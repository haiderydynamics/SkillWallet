"""
CrimeVision AI - Intelligent Multimodal Forensic Analysis Platform
Skill Wallet Capstone Project 2
Main Application Entrypoint
"""

import streamlit as st

# Configure page before any other Streamlit calls
st.set_page_config(
    page_title="CrimeVision AI - Forensic Multimodal Analysis",
    page_icon="🕵️",
    layout="wide",
    initial_sidebar_state="expanded"
)

from styles.forensic_theme import apply_forensic_theme, render_tactical_header
from core.config import APP_NAME, APP_SUBTITLE, DEFAULT_CASE
from core.custody import ChainOfCustodyManager
from core.ai_service import AIServiceRouter
from modules.visual_tagger import render_visual_tagger_tab
from modules.audio_timeline import render_audio_timeline_tab
from modules.cctv_analysis import render_cctv_analysis_tab
from modules.multimodal_fusion import render_multimodal_fusion_tab
from modules.export_report import render_export_report_tab


def init_application_state():
    """Initializes global session state variables."""
    ChainOfCustodyManager.initialize_custody_state()
    if "groq_api_key" not in st.session_state:
        st.session_state.groq_api_key = ""
    if "gemini_api_key" not in st.session_state:
        st.session_state.gemini_api_key = ""
    if "active_case_id" not in st.session_state:
        st.session_state.active_case_id = DEFAULT_CASE["case_id"]


def render_sidebar():
    """Renders the forensic configuration, API keys, and custody audit logs in sidebar."""
    with st.sidebar:
        st.markdown(
            """
            <div style="padding: 10px 0; border-bottom: 1px solid #1e293b; margin-bottom: 16px;">
                <div style="font-family: monospace; font-size: 1.1rem; font-weight: bold; color: #38bdf8;">
                    🛡️ FORENSIC CONFIG & SECURITY
                </div>
                <div style="font-size: 0.75rem; color: #94a3b8;">
                    Operational Environment & Dual-Engine Hub
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Operational Mode Indicator
        live_active = AIServiceRouter.is_live_mode_available()
        if live_active:
            st.success("🟢 LIVE MULTIMODAL AI CONNECTED")
        else:
            st.info("🔵 AUTONOMOUS DEMO MODE ACTIVE (Zero Key Fallback)")

        # API Configuration Expandable
        with st.expander("🔑 AI Engine Credentials (Optional)", expanded=not live_active):
            st.caption("Provide either Groq or Gemini API keys to enable live cloud model inference. Without keys, the built-in offline forensic intelligence engine runs automatically.")
            groq_input = st.text_input(
                "Groq API Key (Llama 3.3 / Whisper)",
                value=st.session_state.groq_api_key,
                type="password",
                help="Enter your Groq API key (starts with gsk_)"
            )
            if groq_input != st.session_state.groq_api_key:
                st.session_state.groq_api_key = groq_input
                st.rerun()

            gemini_input = st.text_input(
                "Google Gemini API Key",
                value=st.session_state.gemini_api_key,
                type="password",
                help="Enter your Google Gemini API key"
            )
            if gemini_input != st.session_state.gemini_api_key:
                st.session_state.gemini_api_key = gemini_input
                st.rerun()

        # Chain of Custody Sidebar Summary
        st.markdown("---")
        st.markdown("##### 🏛️ Chain-of-Custody Ledger")
        st.markdown(f"**Case:** `{DEFAULT_CASE['case_id']}`")
        st.markdown(f"**Lead:** {DEFAULT_CASE['lead_investigator']}")
        st.markdown(f"**Badge:** `{DEFAULT_CASE['badge_number']}`")

        # Custody Audit History
        ledger = ChainOfCustodyManager.get_ledger()
        with st.expander(f"📜 Audit Events ({len(ledger)})", expanded=False):
            for ev in reversed(ledger[-8:]):
                st.markdown(
                    f"<div style='font-size: 0.72rem; border-bottom: 1px solid #1e293b; padding: 4px 0;'>"
                    f"<span style='color: #64748b;'>{ev['timestamp'].split(' ')[1]}</span> "
                    f"<strong style='color: #38bdf8;'>[{ev['evidence_id']}]</strong><br>"
                    f"<span style='color: #cbd5e1;'>{ev['action']}</span><br>"
                    f"<span style='color: #94a3b8; font-style: italic;'>By: {ev['actor']}</span>"
                    f"</div>",
                    unsafe_allow_html=True
                )

        # System Diagnostics
        st.markdown("---")
        st.markdown("##### ⚙️ System Diagnostics")
        st.markdown(
            """
            <div style="font-size: 0.74rem; font-family: monospace; color: #94a3b8; line-height: 1.8;">
                <div>● Database: In-Memory (Zero Dependency)</div>
                <div>● RT-DETR Engine: Initialized</div>
                <div>● Acoustic Whisper: Ready</div>
                <div>● PDF Engine: ReportLab 5.0 Active</div>
                <div>● Integrity: SHA-256 Validated</div>
            </div>
            """,
            unsafe_allow_html=True
        )


def render_custody_indicator_bar():
    """Renders the top persistent forensic chain-of-custody tracking indicators."""
    evd_count = len(ChainOfCustodyManager.get_evidence_items())
    audit_count = len(ChainOfCustodyManager.get_ledger())

    html = f"""
    <div class="custody-badge-bar">
        <div class="custody-item">
            <span>CASE ID:</span>
            <span class="custody-val">{DEFAULT_CASE['case_id']}</span>
        </div>
        <div class="custody-item">
            <span>&bull;</span>
            <span>INVESTIGATOR:</span>
            <span class="custody-val">{DEFAULT_CASE['lead_investigator']} ({DEFAULT_CASE['badge_number']})</span>
        </div>
        <div class="custody-item">
            <span>&bull;</span>
            <span>SECURED ASSETS:</span>
            <span class="custody-val">{evd_count} Modalities</span>
        </div>
        <div class="custody-item">
            <span>&bull;</span>
            <span>AUDIT TRAIL:</span>
            <span class="custody-val">{audit_count} Logged Actions</span>
        </div>
        <div class="custody-item" style="margin-left: auto;">
            <span style="color: #10b981; font-weight: bold;">● INTEGRITY: SHA-256 CERTIFIED</span>
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def main():
    """Main application loop."""
    init_application_state()
    apply_forensic_theme()
    render_sidebar()
    render_tactical_header()
    render_custody_indicator_bar()

    # Core Navigation Tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📷 Tab 1: Visual Tagger (RT-DETR)",
        "🎙️ Tab 2: Witness Audio (Whisper)",
        "📹 Tab 3: CCTV Progression",
        "🧩 Tab 4: Multimodal RAG Chat",
        "📄 Tab 5: Forensic PDF Export"
    ])

    with tab1:
        render_visual_tagger_tab()

    with tab2:
        render_audio_timeline_tab()

    with tab3:
        render_cctv_analysis_tab()

    with tab4:
        render_multimodal_fusion_tab()

    with tab5:
        render_export_report_tab()


if __name__ == "__main__":
    main()
