from sqlalchemy.orm import Session
from tenacity import retry, stop_after_attempt, wait_fixed
from .models import Employee, Attendance
from .logging_config import get_logger

logger = get_logger("crud")


@retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
def create_employee(db: Session, data):
    try:
        employee = Employee(**data.dict())
        db.add(employee)
        db.commit()
        db.refresh(employee)
        logger.info(f"Employee created: {employee.id}")
        return employee
    except Exception as e:
        db.rollback()
        logger.error(f"Create employee failed: {e}")
        raise


def get_all_employees(db: Session):
    return db.query(Employee).all()


def get_employee_by_id(db: Session, employee_id):
    return db.query(Employee).filter(Employee.id == employee_id).first()


@retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
def delete_employee(db: Session, employee_id):
    try:
        employee = get_employee_by_id(db, employee_id)
        if employee:
            db.delete(employee)
            db.commit()
            logger.info(f"Employee deleted: {employee_id}")
        return employee
    except Exception as e:
        db.rollback()
        logger.error(f"Delete employee failed: {e}")
        raise


@retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
def create_attendance(db: Session, data):
    try:
        attendance = Attendance(**data.dict())
        db.add(attendance)
        db.commit()
        db.refresh(attendance)
        logger.info(f"Attendance marked: {attendance.id}")
        return attendance
    except Exception as e:
        db.rollback()
        logger.error(f"Create attendance failed: {e}")
        raise


def get_attendance_for_employee(db: Session, employee_id):
    return db.query(Attendance).filter(
        Attendance.employee_id == employee_id
    ).order_by(Attendance.date.desc()).all()
