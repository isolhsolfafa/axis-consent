"""
AXIS 동의서 QR 이미지 생성
사용: python3 gen_qr.py [URL]
기본 URL: https://axis-consent.netlify.app/
"""
import sys
import qrcode
from qrcode.constants import ERROR_CORRECT_H

url = sys.argv[1] if len(sys.argv) > 1 else "https://axis-consent.netlify.app/"

# 고품질 + 에러 보정 (인쇄용)
qr = qrcode.QRCode(
    version=None,                        # 자동
    error_correction=ERROR_CORRECT_H,    # 30% 복구 — 인쇄 후 일부 손상돼도 인식
    box_size=20,                         # 픽셀 크기 — 인쇄용 큰 사이즈
    border=4,                            # 흰 여백 (표준 4모듈)
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="#2A2D35", back_color="#FFFFFF")
out_path = "AXIS_동의서_QR.png"
img.save(out_path)

print(f"✓ QR 이미지 생성 완료")
print(f"  URL  : {url}")
print(f"  파일 : {out_path}")
print(f"  크기 : {img.size[0]}x{img.size[1]}px")
