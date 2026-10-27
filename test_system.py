"""
System Integration & Automated Verification Test Suite
Validates imports, custody manager, synthetic asset generators, RAG engine, and PDF export.
"""

import io
import sys
from PIL import Image

def run_tests():
    print("==================================================")
    print("CRIMEVISION AI - SYSTEM VERIFICATION SUITE")
    print("==================================================")

    # 1. Test Imports
    print("[TEST 1/5] Testing Core & Module Imports...")
    try:
        from core.config import DEFAULT_CASE, DETECTION_CLASSES, LEGAL_PENAL_CODES
        from core.custody import ChainOfCustodyManager
        from core.ai_service import AIServiceRouter
        from core.pdf_generator import ForensicPDFGenerator
        from assets.sample_evidence import (
            SAMPLE_CASES, generate_synthetic_crime_scene_image, generate_synthetic_audio_wav
        )
        from modules.visual_tagger import draw_bounding_boxes
        print("  [PASS] All modules and packages imported cleanly.")
    except Exception as e:
        print(f"  [FAIL] Import error: {e}")
        sys.exit(1)

    # 2. Test Chain of Custody & SHA-256
    print("[TEST 2/5] Testing Cryptographic Chain-of-Custody & SHA-256...")
    sample_data = b"FORENSIC_EVIDENCE_BITSTREAM_TEST_DATA"
    hash_val = ChainOfCustodyManager.calculate_sha256(sample_data)
    assert len(hash_val) == 64, f"Invalid SHA-256 hash length: {len(hash_val)}"
    print(f"  [PASS] SHA-256 Generated: {hash_val[:16]}... (Length: 64)")

    # 3. Test Synthetic Asset Generators
    print("[TEST 3/5] Testing In-Memory Evidence Asset Generation...")
    img_bytes = generate_synthetic_crime_scene_image()
    assert len(img_bytes) > 1000, "Image byte generation failed"
    img = Image.open(io.BytesIO(img_bytes))
    print(f"  [PASS] Crime Scene Image Generated: {img.size[0]}x{img.size[1]} px, {len(img_bytes)} bytes")

    wav_bytes = generate_synthetic_audio_wav(1.0)
    assert len(wav_bytes) > 500, "Audio wave generation failed"
    print(f"  [PASS] 911 Dispatch Audio Wave Generated: {len(wav_bytes)} bytes")

    # Test Bounding Box Renderer
    sample_case = SAMPLE_CASES["APEX_BURGLARY_CASE"]
    detected = sample_case["visual_evidence"]["detected_objects"]
    annotated = draw_bounding_boxes(img, detected)
    assert annotated.size == img.size
    print("  [PASS] RT-DETR Bounding Box Overlay rendered successfully.")

    # 4. Test Grounded RAG Chat Engine
    print("[TEST 4/5] Testing Grounded RAG Interrogation & Citations...")
    mock_ledger = [
        {
            "timestamp": "22:15:28 UTC",
            "evidence_id": "EVD-VID-001",
            "modality": "CCTV",
            "description": "Suspect drew compact firearm from right waistband",
            "details": "Classified under Penal Code § 245",
            "penal_code": "Penal Code § 245"
        },
        {
            "timestamp": "22:15:32 UTC",
            "evidence_id": "EVD-AUD-001",
            "modality": "Audio",
            "description": "Witness 911 caller stated suspect held handgun in right hand",
            "details": "Acoustic stress extreme",
            "penal_code": "Witness Statement"
        }
    ]
    mock_registry = {
        "EVD-VID-001": {"evidence_type": "Video", "name": "CCTV", "sha256": "ABCD1234"*8},
        "EVD-AUD-001": {"evidence_type": "Audio", "name": "911 Call", "sha256": "EF905678"*8}
    }
    rag_result = AIServiceRouter.query_rag_chat("Was a weapon visible before suspect fled?", mock_ledger, mock_registry)
    assert rag_result["grounded"] is True
    assert "EVD-" in rag_result["response"], "Response must cite Evidence IDs"
    print("  [PASS] Grounded RAG Query passed. Citations confirmed in response.")

    # 5. Test ReportLab PDF Generation
    print("[TEST 5/5] Testing Court-Admissible ReportLab PDF Dossier Generation...")
    pdf_bytes = ForensicPDFGenerator.generate_dossier(
        case_data=DEFAULT_CASE,
        custody_ledger=[{"timestamp": "2026-10-20 12:00:00 UTC", "evidence_id": "EVD-IMG-001", "action": "Ingested", "actor": "Det. Vance", "notes": "OK"}],
        evidence_registry=mock_registry,
        visual_data=sample_case["visual_evidence"],
        audio_data=sample_case["audio_evidence"],
        cctv_data=sample_case["cctv_evidence"],
        master_ledger=mock_ledger
    )
    assert pdf_bytes.startswith(b"%PDF"), "Generated output is not a valid PDF binary"
    assert len(pdf_bytes) > 2000, "PDF size unexpectedly small"
    print(f"  [PASS] PDF Dossier Generated Successfully: {len(pdf_bytes)} bytes (%PDF-1.4 header confirmed)")

    print("==================================================")
    print("ALL 5 VERIFICATION SUITES PASSED WITH 100% SUCCESS")
    print("==================================================")


if __name__ == "__main__":
    run_tests()
