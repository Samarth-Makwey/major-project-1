import "./Navbar.css"

export default function Navbar() {
  return (
    <nav className="navbar">
      <div className="logo">DARA</div>

      <ul className="nav-links">
        <li>Home</li>
        <li>Datasets</li>
        <li>About</li>
      </ul>
    </nav>
  );
}
