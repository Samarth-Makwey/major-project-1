import './About.css';
import Navbar from '../../components/Navbar/Navbar';
import Footer from '../../components/Footer/Footer';

function AboutPage() {
  return (
    <div className="about-page-root">
      <Navbar />
      <div className="about-page">
        <div className="about-header">
          <h1>About Us</h1>
          <p>Learn more about our data platform and mission</p>
        </div>

        <div className="about-container">
          <section className="about-section">
            <h2>Our Mission</h2>
            <p>
              We believe that quality data should be accessible to everyone. Our platform makes it easy for developers and businesses to discover, query, and integrate high-quality datasets through a single, developer-friendly API.
            </p>
          </section>

          <section className="about-section">
            <h2>What We Offer</h2>
            <ul>
              <li>✓ Clean, well-structured datasets</li>
              <li>✓ Fast and reliable RESTful APIs</li>
              <li>✓ Comprehensive documentation</li>
            </ul>
          </section>

          <section className="about-section">
            <h2>Our Technology</h2>
            <p>
              Built with modern technologies including Python, Pandas for data processing, and a robust REST API architecture. We ensure reliability, scalability, and performance across all our services.
            </p>
          </section>

          <section className="about-section">
            <h2>Get Started Today</h2>
            <p>
              Join thousands of developers who are building amazing applications with our data API platform. Start your free trial today and experience the difference quality data makes.
            </p>
            <button className="btn btn-primary">Start Free Trial</button>
          </section>
        </div>
      </div>
      <Footer />
    </div>
  );
}

export default AboutPage;
