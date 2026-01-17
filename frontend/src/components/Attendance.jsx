import { useEffect, useState } from "react";
import { api } from "../api";

export default function Attendance() {
  const [employees, setEmployees] = useState([]);
  const [employeeId, setEmployeeId] = useState("");
  const [date, setDate] = useState("");
  const [status, setStatus] = useState("Present");
  const [records, setRecords] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    api.get("/employees/").then((res) => setEmployees(res.data));
  }, []);

  const fetchAttendance = async (id) => {
    const res = await api.get(`/attendance/${id}`);
    setRecords(res.data);
  };

  const markAttendance = async () => {
    setError("");
    try {
      await api.post("/attendance/", {
        employee_id: employeeId,
        date,
        status,
      });
      fetchAttendance(employeeId);
    } catch (err) {
      setError(err.response?.data?.detail || "Failed to mark attendance");
    }
  };

  return (
    <>
      <h3>Attendance</h3>

      {error && <div className="error">{error}</div>}

      <select onChange={(e) => {
        setEmployeeId(e.target.value);
        fetchAttendance(e.target.value);
      }}>
        <option value="">Select Employee</option>
        {employees.map((e) => (
          <option key={e.id} value={e.id}>
            {e.full_name}
          </option>
        ))}
      </select>

      <input type="date" onChange={(e) => setDate(e.target.value)} />

      <select onChange={(e) => setStatus(e.target.value)}>
        <option value="Present">Present</option>
        <option value="Absent">Absent</option>
      </select>

      <button onClick={markAttendance}>Mark Attendance</button>

      <h4>Attendance Records</h4>

      {records.length === 0 && <p>No records available</p>}

      {records.map((r) => (
        <div key={r.id}>
          {r.date} —{" "}
          <span className={r.status === "Present" ? "status-present" : "status-absent"}>
            {r.status}
          </span>
        </div>
      ))}
    </>
  );
}
