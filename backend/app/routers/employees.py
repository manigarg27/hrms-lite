from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from ..database import SessionLocal
from ..schemas import EmployeeCreate, EmployeeResponse
from ..models import Employee
from ..crud import create_employee, get_all_employees, delete_employee
from ..logging_config import get_logger

logger = get_logger("employees")

router = APIRouter(prefix="/employees", tags=["Employees"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=EmployeeResponse, status_code=201)
def add_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    try:
        existing = db.query(Employee).filter(
            (Employee.email == employee.email) |
            (Employee.employee_id == employee.employee_id)
        ).first()

        if existing:
            raise HTTPException(
                status_code=409,
                detail="Employee with same email or employee ID already exists"
            )

        return create_employee(db, employee)

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Add employee error: {e}")
        raise HTTPException(status_code=500, detail="Failed to create employee")


@router.get("/", response_model=list[EmployeeResponse])
def list_employees(db: Session = Depends(get_db)):
    return get_all_employees(db)


@router.delete("/{id}")
def remove_employee(id: UUID, db: Session = Depends(get_db)):
    try:
        employee = delete_employee(db, id)
        if not employee:
            raise HTTPException(status_code=404, detail="Employee not found")
        return {"message": "Employee deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Delete employee error: {e}")
        raise HTTPException(status_code=500, detail="Failed to delete employee")
