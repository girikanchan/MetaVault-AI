import base64
import re
from pathlib import Path
from textwrap import dedent

import streamlit as st  # pyright: ignore[reportMissingImports]


# -------------------------------------------------------------------
# Page Config
# -------------------------------------------------------------------
st.set_page_config(
    page_title="MetaVault AI",
    page_icon=":sparkles:",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def image_to_base64(path: str) -> str:
    """Return base64 for image if present, otherwise empty string."""
    img_path = Path(path)
    
    if not img_path.exists():
        return ""
    return base64.b64encode(img_path.read_bytes()).decode("utf-8")


logo_b64 = image_to_base64("frontend/assets/logo.png")


def render_html(raw_html: str) -> None:
    """Render HTML safely without markdown code-block side effects."""
    cleaned = dedent(raw_html).strip()
    cleaned = re.sub(r">\s+<", "><", cleaned)
    st.markdown(cleaned, unsafe_allow_html=True)


# -------------------------------------------------------------------
# CSS
# -------------------------------------------------------------------
st.markdown(
    dedent("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css');

    :root {
      --bg-dark-1: #030817;
      --bg-dark-2: #060f29;
      --bg-dark-3: #0a1335;
      --cyan: #00e5ff;
      --purple: #7b61ff;
      --text-main: #f3f7ff;
      --text-soft: #afbdd8;
      --text-muted: #8f9ab3;
      --line-soft: rgba(134, 164, 224, 0.22);
      --line-card: rgba(0, 229, 255, 0.44);
      --card-bg: rgba(8, 18, 47, 0.64);
      --shadow-cyan: 0 0 22px rgba(0, 229, 255, 0.34);
      --shadow-purple: 0 0 26px rgba(123, 97, 255, 0.31);
      --gradient-main: linear-gradient(95deg, #00d7ff 0%, #2f96ff 52%, #775fff 100%);
      --gradient-glass: linear-gradient(140deg, rgba(0,229,255,0.08), rgba(123,97,255,0.11));
    }

    html, body, [class*="css"] {
      font-family: 'Inter', sans-serif;
    }

    .stApp {
      background:
        radial-gradient(1180px 760px at -8% -24%, rgba(0,229,255,0.2), transparent 58%),
        radial-gradient(980px 670px at 112% 22%, rgba(123,97,255,0.24), transparent 54%),
        linear-gradient(180deg, var(--bg-dark-1) 0%, var(--bg-dark-2) 42%, #060d24 100%);
      color: var(--text-main);
    }

    [data-testid="stHeader"], [data-testid="stToolbar"] {
      background: transparent !important;
    }

    [data-testid="stAppViewContainer"] > .main {
      padding-top: 0.15rem;
    }

    .block-container {
      max-width: 1360px;
      padding-top: 0.8rem;
      padding-bottom: 2.4rem;
      padding-left: 2.2rem;
      padding-right: 2.2rem;
    }

    /* Generic */
    .mv-link {
      color: inherit;
      text-decoration: none;
    }
    .gradient-text {
      background: var(--gradient-main);
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent;
      display: inline-block;
    }
    .mv-card-glass {
      background: var(--card-bg);
      border: 1px solid var(--line-soft);
      backdrop-filter: blur(8px);
    }
    .soft-pill {
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      border: 1px solid rgba(0,229,255,0.5);
      background: rgba(0, 229, 255, 0.1);
      color: #cbfbff;
      border-radius: 999px;
      padding: 0.42rem 0.88rem;
      font-size: 0.75rem;
      font-weight: 600;
      letter-spacing: 0.04em;
    }
    .soft-pill .dot {
      color: #82efff;
      font-size: 0.67rem;
      opacity: 0.92;
    }

    /* Shell */
    # .page-shell {
    #   border: 1px solid rgba(125, 152, 206, 0.25);
    #   border-radius: 20px;
    #   background:
    #     linear-gradient(180deg, rgba(255,255,255,0.018) 0%, rgba(255,255,255,0.00) 100%),
    #     radial-gradient(920px 430px at 8% 0%, rgba(43,72,128,0.26), transparent 61%),
    #     linear-gradient(180deg, #060c24 0%, #040916 100%);
    #   box-shadow: 0 0 0 1px rgba(124,151,204,0.1) inset;
    #   padding: 1.2rem 1.2rem 1.4rem 1.2rem;
    # }

    # .light-shell {
    #   margin-top: 0.55rem;
    #   border-radius: 16px;
    #   padding: 1.05rem 1.05rem 0.7rem 1.05rem;
    #   border: 1px solid rgba(198, 213, 239, 0.95);
    #   background: linear-gradient(180deg, #ffffff 0%, #f6faff 100%);
    #   box-shadow: 0 16px 32px rgba(2, 16, 50, 0.18);
    #   min-height: 300px;
    # }

    /* Navbar */
    .mv-nav {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1rem;
      padding: 0.22rem 0.32rem 0.9rem 0.32rem;
    }
    .nav-left {
      display: flex;
      align-items: center;
      gap: 0.7rem;
      min-width: 300px;
    }
    .logo-box {
      width: 50px;
      height: 50px;
      border-radius: 14px;
      background: linear-gradient(160deg, rgba(0,229,255,0.24), rgba(123,97,255,0.28));
      border: 1px solid rgba(0,229,255,0.5);
      display: grid;
      place-items: center;
      box-shadow: var(--shadow-cyan);
      overflow: hidden;
    }
    .logo-box i {
      color: #93f7ff;
      font-size: 1.2rem;
    }
    .logo-box img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }
    .brand-wrap {
      display: flex;
      flex-direction: column;
      line-height: 1.0;
    }
    .brand-title {
      font-size: 2.02rem;
      font-weight: 800;
      letter-spacing: 0.002em;
      color: #f3f8ff;
      margin: 0;
    }
    .brand-title .ai {
      color: #24a2ff;
    }
    .brand-subtitle {
      margin-top: 0.14rem;
      font-size: 0.62rem;
      color: #a8bade;
      letter-spacing: 0.125em;
      font-weight: 700;
    }
    .nav-right {
      display: flex;
      align-items: center;
      gap: 1.08rem;
      flex-wrap: wrap;
      justify-content: flex-end;
    }
    .nav-links {
      display: flex;
      align-items: center;
      gap: 1.2rem;
      flex-wrap: wrap;
    }
    .nav-links a {
      font-size: 0.9rem;
      color: #d5e0f6;
      font-weight: 500;
      text-decoration: none;
      transition: all .2s ease;
    }
    .nav-links a:hover {
      color: #ffffff;
      text-shadow: 0 0 12px rgba(123,97,255,0.5);
    }
    .cta-btn {
      color: #fff !important;
      text-decoration: none;
      font-weight: 700;
      font-size: 0.93rem;
      background: var(--gradient-main);
      border: 1px solid rgba(255,255,255,0.22);
      border-radius: 12px;
      padding: 0.68rem 1.15rem;
      box-shadow: 0 10px 24px rgba(5,26,80,0.45), var(--shadow-purple);
      white-space: nowrap;
      display: inline-flex;
      align-items: center;
      gap: .5rem;
      transition: transform .2s ease;
    }
    .cta-btn:hover {
      transform: translateY(-1px);
    }

    /* Hero */
    .hero-grid {
      display: grid;
      grid-template-columns: 1.09fr 1.12fr;
      gap: 1.08rem;
      margin-top: 0.06rem;
    }
    .hero-left {
      padding: 0.22rem 0.52rem 0.7rem 0.46rem;
    }
    .hero-title {
      margin: 0.86rem 0 0.66rem 0;
      font-size: clamp(2rem, 3.55vw, 3.86rem);
      line-height: 1.01;
      font-weight: 900;
      letter-spacing: -0.02em;
      max-width: 640px;
    }
    .hero-copy {
      color: #d5def2;
      font-size: 1.14rem;
      line-height: 1.34;
      max-width: 640px;
      margin-top: 0.74rem;
    }
    .hero-buttons {
      display: flex;
      gap: 0.72rem;
      margin-top: 1.16rem;
      flex-wrap: wrap;
    }
    .btn-main, .btn-alt {
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: .52rem;
      border-radius: 12px;
      font-weight: 700;
      padding: 0.73rem 1.16rem;
      font-size: 0.97rem;
      transition: all .2s ease;
    }
    .btn-main {
      color: #fff !important;
      border: 1px solid rgba(255,255,255,0.2);
      background: var(--gradient-main);
      box-shadow: var(--shadow-cyan);
    }
    .btn-alt {
      color: #eef3ff;
      border: 1px solid rgba(170,190,228,0.4);
      background: rgba(18, 29, 63, 0.9);
      box-shadow: 0 0 0 1px rgba(255,255,255,0.05) inset;
    }
    .btn-main:hover, .btn-alt:hover {
      transform: translateY(-1px);
    }
    .hero-tags {
      margin-top: 1.1rem;
      display: flex;
      flex-wrap: wrap;
      gap: 1.12rem;
    }
    .hero-tag {
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      color: #bad0f5;
      font-size: 0.92rem;
      font-weight: 600;
    }
    .hero-tag i {
      color: #6ceeff;
      font-size: 0.95rem;
    }

    /* Flow / right diagram */
    .flow-area {
      padding: 0.34rem 0.24rem 0.06rem 0.08rem;
    }
    .flow-top {
      display: grid;
      grid-template-columns: 1fr auto 1fr auto 1fr auto 1fr;
      align-items: stretch;
      gap: 0.64rem;
      margin-bottom: 0.62rem;
    }
    .flow-card {
      position: relative;
      min-height: 168px;
      border-radius: 13px;
      padding: 0.62rem 0.72rem;
      background: linear-gradient(170deg, rgba(4,20,58,0.92), rgba(7,14,32,0.88));
      border: 1px solid var(--line-card);
      box-shadow: 0 0 0 1px rgba(255,255,255,0.045) inset, var(--shadow-cyan);
    }
    .flow-card.purple {
      border-color: rgba(123,97,255,0.62);
      box-shadow: 0 0 0 1px rgba(255,255,255,0.03) inset, var(--shadow-purple);
    }
    .flow-card h4 {
      margin: 0.08rem 0 0.45rem 0;
      color: #95f5ff;
      font-size: 0.9rem;
      letter-spacing: 0.05em;
      text-align: center;
      font-weight: 700;
    }
    .flow-card.purple h4 {
      color: #d1c6ff;
    }
    .flow-card ul {
      margin: 0;
      padding: 0;
      list-style: none;
      color: #e6f0ff;
      font-size: 0.79rem;
      display: flex;
      flex-direction: column;
      gap: .38rem;
      text-align: center;
    }
    .flow-card ul li {
      opacity: 0.95;
    }
    .flow-card .icon-row {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.52rem;
      margin-bottom: 0.32rem;
      color: #90edff;
      font-size: 0.93rem;
    }
    .flow-card .sat-grid {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: .24rem;
      margin-top: .55rem;
    }
    .flow-card .sat-grid span {
      height: 12px;
      border-radius: 4px;
      border: 1px solid rgba(0,229,255,0.45);
      background: rgba(0,229,255,0.1);
      display: block;
    }
    .arrow {
      display: grid;
      place-items: center;
      color: #9be5ff;
      font-size: 1.12rem;
      font-weight: 700;
      text-shadow: 0 0 16px rgba(0,229,255,0.58);
      min-width: 18px;
    }

    .flow-mid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 0.52rem;
      margin-top: 0.18rem;
    }
    .long-card {
      border-radius: 13px;
      padding: 0.62rem 0.85rem;
      background: linear-gradient(140deg, rgba(8,34,69,0.94), rgba(7,15,39,0.9));
      border: 1px solid rgba(0,229,255,0.45);
      box-shadow: 0 0 0 1px rgba(255,255,255,0.038) inset, var(--shadow-cyan);
    }
    .long-card h4 {
      margin: 0;
      text-align: center;
      font-size: 0.96rem;
      font-weight: 800;
      color: #89f1ff;
      letter-spacing: 0.04em;
    }
    .long-card .row {
      margin-top: .36rem;
      display: flex;
      gap: 0.9rem;
      justify-content: center;
      color: #deedff;
      font-size: 0.78rem;
      font-weight: 500;
      flex-wrap: wrap;
    }
    .long-card .row i {
      color: #90eeff;
      margin-right: .35rem;
    }
    .long-card.purple {
      border-color: rgba(123,97,255,0.6);
      box-shadow: 0 0 0 1px rgba(255,255,255,0.03) inset, var(--shadow-purple);
    }

    /* Features */
    .features-wrap {
      margin-top: 0.18rem;
      padding-top: 0.26rem;
      border-radius: 16px;
      padding: 1.05rem 1.05rem 0.7rem 1.05rem;
      border: 1px solid rgba(198, 213, 239, 0.95);
      background: linear-gradient(180deg, #ffffff 0%, #f6faff 100%);
      box-shadow: 0 16px 32px rgba(2, 16, 50, 0.18);
      min-height: 300px;
    }
    .features-title {
      text-align: center;
      font-size: 2.02rem;
      font-weight: 800;
      letter-spacing: -0.01em;
      margin: 0.12rem 0 1.02rem 0;
      color: #17284e;
    }
    .features-grid {
      display: grid;
      grid-template-columns: repeat(6, minmax(0, 1fr));
      gap: 0.68rem;
    }
    .feature-card {
      border-radius: 14px;
      padding: 0.86rem 0.72rem 0.84rem 0.72rem;
      background: linear-gradient(180deg, #ffffff, #fafdff);
      border: 1px solid rgba(185, 202, 231, 0.82);
      text-align: center;
      min-height: 150px;
      box-shadow: 0 8px 18px rgba(23, 54, 117, 0.085);
      transition: border-color .2s ease, transform .2s ease, box-shadow .2s ease;
    }
    .feature-card:hover {
      border-color: rgba(0,229,255,0.45);
      transform: translateY(-2px);
      box-shadow: 0 10px 22px rgba(15, 68, 138, 0.14);
    }
    .feature-icon {
      font-size: 1.62rem;
      margin-top: 0.1rem;
      color: #2ea8ff;
      text-shadow: 0 0 16px rgba(46,168,255,0.26);
    }
    .feature-title {
      margin-top: 0.52rem;
      font-size: 0.95rem;
      font-weight: 700;
      color: #1c335d;
      line-height: 1.25;
      min-height: 2.5em;
    }
    .feature-copy {
      margin-top: 0.36rem;
      font-size: 0.75rem;
      line-height: 1.33;
      color: #53688d;
    }

    /* Platforms */
    .platform-row {
      margin-top: 0.9rem;
      border-radius: 14px;
      border: 1px solid rgba(186, 204, 231, 0.85);
      background: linear-gradient(180deg, #ffffff, #f6faff);
      padding: 0.72rem 0.92rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      flex-wrap: wrap;
    }
    .platform-label {
      font-size: 0.94rem;
      font-weight: 800;
      color: #1f3159;
      letter-spacing: 0.05em;
      min-width: 270px;
      text-transform: uppercase;
    }
    .platforms {
      display: flex;
      align-items: center;
      justify-content: flex-end;
      gap: 1rem;
      flex-wrap: wrap;
      color: #273f68;
    }
    .platform-item {
      display: inline-flex;
      align-items: center;
      gap: .46rem;
      font-size: 0.98rem;
      font-weight: 700;
      color: #233b63;
      opacity: .97;
      white-space: nowrap;
    }
    .platform-item i {
      color: #2b92ff;
      font-size: 0.94rem;
    }

    /* Responsive */
    @media (max-width: 1320px) {
      .hero-title {
        font-size: clamp(2rem, 3.2vw, 3.28rem);
      }
      .features-grid {
        grid-template-columns: repeat(3, minmax(0, 1fr));
      }
    }
    @media (max-width: 1120px) {
      .hero-grid {
        grid-template-columns: 1fr;
      }
      .flow-top {
        grid-template-columns: 1fr;
        gap: 0.6rem;
      }
      .arrow {
        transform: rotate(90deg);
        min-height: 20px;
      }
      .nav-right {
        justify-content: flex-start;
      }
    }
    @media (max-width: 820px) {
      .block-container {
        padding-left: 1.1rem;
        padding-right: 1.1rem;
      }
      .brand-title {
        font-size: 1.42rem;
      }
      .brand-subtitle {
        letter-spacing: .08em;
      }
      .features-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
      }
      .hero-copy {
        font-size: 1.04rem;
      }
      .features-title {
        font-size: 1.7rem;
      }
    }
    @media (max-width: 520px) {
      .features-grid {
        grid-template-columns: 1fr;
      }
      .platform-label {
        min-width: auto;
      }
    }
    </style>
    """),
    unsafe_allow_html=True,
)


# -------------------------------------------------------------------
# Main Wrapper
# -------------------------------------------------------------------
st.markdown('<div class="page-shell">', unsafe_allow_html=True)


# -------------------------------------------------------------------
# 1) Top Navigation Bar
# -------------------------------------------------------------------
render_html(f"""
    <div class="mv-nav">
      <div class="nav-left">
        <div class="logo-box">
          {"<img src='data:image/png;base64," + logo_b64 + "' alt='MetaVault AI logo' />" if logo_b64 else "<i class='fa-solid fa-cubes'></i>"}
        </div>
        <div class="brand-wrap">
          <div class="brand-title">MetaVault <span class="ai">AI</span></div>
          <div class="brand-subtitle">AI-POWERED METADATA ENGINEERING</div>
        </div>
      </div>
      <div class="nav-right">
        <div class="nav-links">
          <a href="#" class="mv-link">Features</a>
          <a href="#" class="mv-link">How It Works</a>
          <a href="#" class="mv-link">Use Cases</a>
          <a href="#" class="mv-link">Architecture</a>
          <a href="#" class="mv-link">Pricing</a>
          <a href="#" class="mv-link">Docs</a>
          <a href="#" class="mv-link">About</a>
        </div>
        <a href="#" class="cta-btn">Let's Start <i class="fa-solid fa-arrow-right-long"></i></a>
      </div>
    </div>
    """)


# -------------------------------------------------------------------
# 2) Hero Section
# -------------------------------------------------------------------
render_html("""
    <div class="hero-grid">
      <div class="hero-left">
        <div class="soft-pill">
          <span>LLM-POWERED</span>
          <span class="dot"><i class="fa-solid fa-diamond"></i></span>
          <span>SMART</span>
          <span class="dot"><i class="fa-solid fa-diamond"></i></span>
          <span>GOVERNED</span>
        </div>

        <h1 class="hero-title">
          Automate Metadata Engineering with
          <span class="gradient-text">AI Intelligence</span>
        </h1>

        <div class="hero-copy">
          Transform schemas into trusted Data Vault models using LLMs,
          validation, and human-in-the-loop approval.<br>
          Build governed metadata. Accelerate your data journey.
        </div>

        <div class="hero-buttons">
          <a href="#" class="btn-main">Let's Start <i class="fa-solid fa-arrow-right-long"></i></a>
          <a href="#" class="btn-alt">View Demo <i class="fa-solid fa-circle-play"></i></a>
        </div>

        <div class="hero-tags">
          <div class="hero-tag"><i class="fa-solid fa-microchip"></i>AI-Powered</div>
          <div class="hero-tag"><i class="fa-solid fa-shield-heart"></i>Human-Governed</div>
          <div class="hero-tag"><i class="fa-solid fa-badge-check"></i>Production-Ready</div>
        </div>
      </div>

      <div class="flow-area">
        <div class="flow-top">
          <div class="flow-card">
            <h4>SCHEMA</h4>
            <div class="icon-row"><i class="fa-solid fa-database"></i></div>
            <ul>
              <li>Tables</li>
              <li>Columns</li>
              <li>Relationships</li>
            </ul>
          </div>
          <div class="arrow"><i class="fa-solid fa-arrow-right"></i></div>

          <div class="flow-card purple">
            <h4>LLM PROCESSING</h4>
            <div class="icon-row"><i class="fa-solid fa-brain"></i></div>
            <ul>
              <li>Understand Schema</li>
              <li>Detect Keys &amp; Relationships</li>
              <li>Generate Metadata</li>
            </ul>
          </div>
          <div class="arrow"><i class="fa-solid fa-arrow-right"></i></div>

          <div class="flow-card">
            <h4>DATA VAULT MODEL</h4>
            <div class="icon-row">
              <i class="fa-solid fa-cube"></i>
              <i class="fa-solid fa-circle-nodes"></i>
              <i class="fa-solid fa-link"></i>
            </div>
            <ul>
              <li>HUB</li>
              <li>LINKS</li>
              <li>SATELLITES</li>
            </ul>
            <div class="sat-grid">
              <span></span><span></span><span></span><span></span><span></span>
            </div>
          </div>
          <div class="arrow"><i class="fa-solid fa-arrow-right"></i></div>

          <div class="flow-card">
            <h4>BUSINESS IMPACT</h4>
            <div class="icon-row"><i class="fa-solid fa-chart-line"></i></div>
            <ul>
              <li>Trusted Metadata</li>
              <li>Faster Delivery</li>
              <li>Better Governance</li>
              <li>Analytics Ready</li>
            </ul>
          </div>
        </div>

        <div class="flow-mid">
          <div class="long-card">
            <h4>VALIDATION &amp; APPROVAL</h4>
            <div class="row">
              <span><i class="fa-solid fa-shield-check"></i>Rule Validation</span>
              <span><i class="fa-solid fa-user-check"></i>Human Approval</span>
            </div>
          </div>
          <div class="long-card purple">
            <h4>METADATA STORE</h4>
            <div class="row">
              <span><i class="fa-solid fa-box-archive"></i>Versioned</span>
              <span><i class="fa-solid fa-scale-balanced"></i>Governed</span>
              <span><i class="fa-solid fa-clipboard-list"></i>Auditable</span>
            </div>
          </div>
        </div>
      </div>
    </div>
    """)


# -------------------------------------------------------------------
# 3) Features Section
# -------------------------------------------------------------------
st.markdown('<div class="light-shell">', unsafe_allow_html=True)

render_html("""
    <div class="features-wrap">
      <div class="features-title">
        Everything You Need for
        <span class="gradient-text">Intelligent Metadata Engineering</span>
      </div>

      <div class="features-grid">
        <div class="feature-card">
          <div class="feature-icon"><i class="fa-solid fa-brain"></i></div>
          <div class="feature-title">AI-Powered Modeling</div>
          <div class="feature-copy">
            LLMs analyze schemas and automatically generate Data Vault structures.
          </div>
        </div>

        <div class="feature-card">
          <div class="feature-icon"><i class="fa-solid fa-project-diagram"></i></div>
          <div class="feature-title">Smart Relationships</div>
          <div class="feature-copy">
            Detect business keys, links, and attribute classifications intelligently.
          </div>
        </div>

        <div class="feature-card">
          <div class="feature-icon"><i class="fa-solid fa-shield-halved"></i></div>
          <div class="feature-title">Validation Engine</div>
          <div class="feature-copy">
            Rule-based validation ensures metadata quality and consistency.
          </div>
        </div>

        <div class="feature-card">
          <div class="feature-icon"><i class="fa-solid fa-users"></i></div>
          <div class="feature-title">Human-in-the-Loop</div>
          <div class="feature-copy">
            Review, edit, and approve metadata with an intuitive interface.
          </div>
        </div>

        <div class="feature-card">
          <div class="feature-icon"><i class="fa-solid fa-database"></i></div>
          <div class="feature-title">Versioned Storage</div>
          <div class="feature-copy">
            Store metadata with versioning, audit trails, and full lineage tracking.
          </div>
        </div>

        <div class="feature-card">
          <div class="feature-icon"><i class="fa-solid fa-rocket"></i></div>
          <div class="feature-title">Pipeline Ready</div>
          <div class="feature-copy">
            Seamlessly integrate with PySpark, Fabric, and modern data platforms.
          </div>
        </div>
      </div>
      <div class="platform-row">
        <div class="platform-label">BUILT FOR MODERN DATA PLATFORMS</div>
        <div class="platforms">
          <div class="platform-item"><i class="fa-brands fa-microsoft"></i>Microsoft Fabric</div>
          <div class="platform-item"><i class="fa-solid fa-a"></i>Azure OpenAI</div>
          <div class="platform-item"><i class="fa-solid fa-bolt"></i>PySpark</div>
          <div class="platform-item"><i class="fa-solid fa-mountain-sun"></i>Delta Lake</div>
          <div class="platform-item"><i class="fa-solid fa-water"></i>Streamlit</div>
          <div class="platform-item"><i class="fa-solid fa-database"></i>SQLite</div>
        </div>
      </div>
    </div>
    """)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)


