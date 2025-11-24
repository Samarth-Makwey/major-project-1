import './title.css';

function Title() {
  return (
    <header className="hero">
      <div className="hero-inner">
        <h1 className="hero-title">Data API Platform</h1>
        <p className="hero-subtitle">
          Discover, query, and integrate high-quality datasets with a single,
          developer-friendly API. Fast access, consistent schemas, and secure
          delivery — so your team can build faster.
        </p>

        <div className="hero-ctas">
          <a className="btn btn-primary" href="#get-started">Get started</a>
          
        </div>
      </div>
    </header>
  );
}

export default Title;