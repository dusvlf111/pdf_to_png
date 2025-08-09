import os
import glob
from pdf2image import convert_from_path
import time

def process_pdfs_to_folders(input_folder, output_folder, poppler_bin_path):
    """
    입력 폴더의 PDF를 변환하고, 성공 시 output 폴더에 개별 폴더를 생성해
    PNG와 원본 PDF를 함께 저장합니다.

    :param input_folder: PDF 파일들이 있는 입력 폴더 경로
    :param output_folder: 결과물을 저장할 최상위 출력 폴더 경로
    :param poppler_bin_path: Poppler의 bin 디렉터리 경로
    """
    # 입력 폴더 확인 및 생성
    if not os.path.exists(input_folder):
        os.makedirs(input_folder)
        print(f"'{input_folder}' 폴더가 없어 새로 생성했습니다. 변환할 PDF를 넣어주세요. 🤷‍♂️")
        return

    # 최상위 출력 폴더 생성
    os.makedirs(output_folder, exist_ok=True)

    # 변환할 PDF 파일 목록 가져오기
    pdf_files = glob.glob(os.path.join(input_folder, "*.pdf"))

    if not pdf_files:
        print(f"'{input_folder}'에서 변환할 PDF 파일을 찾을 수 없습니다.")
        return

    total_files = len(pdf_files)
    print(f"총 {total_files}개의 PDF 파일 처리를 시작합니다...")
    start_time = time.time()
    successful_conversions = 0
    
    # 각 파일을 순회하며 변환
    for index, pdf_path in enumerate(pdf_files):
        base_filename = os.path.basename(pdf_path)
        filename_without_ext = os.path.splitext(base_filename)[0]
        
        # 1. 결과물을 저장할 하위 폴더 경로 설정
        result_subfolder = os.path.join(output_folder, filename_without_ext)

        print(f"\n[{index + 1}/{total_files}] '{base_filename}' 처리 중...")

        try:
            # PDF를 이미지 리스트로 변환
            images = convert_from_path(pdf_path, poppler_path=poppler_bin_path)

            # 2. 결과물 하위 폴더 생성
            os.makedirs(result_subfolder, exist_ok=True)

            # 3. 각 페이지를 PNG 파일로 하위 폴더에 저장
            for i, image in enumerate(images):
                output_filename = f"page_{i + 1}.png" # 파일 이름을 더 간단하게 page_N.png로 변경
                image_path = os.path.join(result_subfolder, output_filename)
                image.save(image_path, 'PNG')

            print(f"✅ 변환 완료! ({len(images)} 페이지) -> '{result_subfolder}'")
            successful_conversions += 1

            # 4. 원본 PDF 파일을 결과물 폴더로 이동 (삭제 대신)
            destination_pdf_path = os.path.join(result_subfolder, base_filename)
            os.rename(pdf_path, destination_pdf_path)
            print(f"📄 원본 PDF 파일 '{base_filename}'을(를) 결과 폴더로 이동했습니다.")

        except Exception as e:
            print(f"❌ 오류 발생: {e}")
            print("--> 변환에 실패하여 원본 파일은 이동되지 않습니다.")

    # 최종 결과 요약
    end_time = time.time()
    print("\n" + "="*40)
    print("✨ 모든 작업이 완료되었습니다! ✨")
    print(f"  - 총 작업 시간: {end_time - start_time:.2f}초")
    print(f"  - 성공 (및 이동): {successful_conversions}개")
    print(f"  - 실패: {total_files - successful_conversions}개")
    print("="*40)


# --- 실행 부분 ---
if __name__ == "__main__":
    # ✒️️ 설정: Poppler의 'bin' 폴더 경로를 지정하세요.
    POPPLE_PATH_CONFIG = r"poppler-24.08.0\Library\bin"

    # PDF 파일이 저장된 입력 폴더
    input_dir = "input"

    # 결과물을 저장할 최상위 출력 폴더
    output_dir = "output"

    # 함수 호출
    process_pdfs_to_folders(input_dir, output_dir, POPPLE_PATH_CONFIG)