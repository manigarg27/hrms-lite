import EmployeeForm from "./components/EmployeeForm";
import EmployeeList from "./components/EmployeeList";
import Attendance from "./components/Attendance";

export default function App() {
  return (
    <div className="container">
      <header className="header">
        <h1>HRMS Lite</h1>
        <p>Internal Human Resource Management System</p>
      </header>

      <section className="card">
        <EmployeeForm />
      </section>

      <section className="card">
        <EmployeeList />
      </section>

      <section className="card">
        <Attendance />
      </section>
    </div>
  );
}
