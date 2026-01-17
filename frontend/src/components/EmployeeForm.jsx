import { useState } from "react";
import { api } from "../api";

export default function EmployeeForm() {
  const [form, setForm] = useState({
    employee_id: "",
    full_name: "",
    email: "",
    department: "",
  });

  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const submit = async () => {
    setError("");
    setLoading(true);
    try {
      await api.post("/employees/", form);
      window.location.reload();
    } catch (err) {
      setError(err.response?.data?.detail || "Failed to add employee");
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <h3>Add Employee</h3>

      {error && <div className="error">{error}</div>}

      <input name="employee_id" placeholder="Employee ID" onChange={handleChange} />
      <input name="full_name" placeholder="Full Name" onChange={handleChange} />
      <input name="email" placeholder="Email" onChange={handleChange} />
      <input name="department" placeholder="Department" onChange={handleChange} />

      <button onClick={submit} disabled={loading}>
        {loading ? "Saving..." : "Add Employee"}
      </button>
    </>
  );
}
