import { useEffect, useState } from "react";
import { api } from "../api";

export default function EmployeeList() {
  const [employees, setEmployees] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.get("/employees/")
      .then((res) => setEmployees(res.data))
      .finally(() => setLoading(false));
  }, []);

  const remove = async (id) => {
    await api.delete(`/employees/${id}`);
    setEmployees(employees.filter((e) => e.id !== id));
  };

  return (
    <>
      <h3>Employees</h3>

      {loading && <div className="loading">Loading employees...</div>}
      {!loading && employees.length === 0 && <p>No employees found</p>}

      {employees.map((e) => (
        <div key={e.id} className="employee-item">
          <div>
            <strong>{e.full_name}</strong>
            <div>{e.department}</div>
          </div>
          <button className="secondary" onClick={() => remove(e.id)}>
            Delete
          </button>
        </div>
      ))}
    </>
  );
}
