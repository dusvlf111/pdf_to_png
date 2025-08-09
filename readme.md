# PDF 자동 변환 및 정리 스크립트

이 프로젝트는 `input` 폴더에 있는 모든 PDF 파일을 감지하여 각 파일을 PNG 이미지로 변환하고, 성공 시 원본 PDF와 결과물을 `output` 폴더에 깔끔하게 정리해주는 파이썬 스크립트입니다.



## 주요 기능

-   **일괄 처리**: `input` 폴더 내의 모든 PDF 파일을 한 번에 처리합니다.
-   **자동 폴더 생성**: 변환에 성공한 각 PDF에 대해 `output` 폴더 내에 별도의 하위 폴더를 생성합니다.
-   **결과물 통합 관리**: 생성된 PNG 이미지들과 원본 PDF 파일을 하나의 결과 폴더로 함께 이동시켜 관리의 용이성을 높입니다.
-   **오류 처리**: 변환에 실패한 파일은 `input` 폴더에 그대로 남아있어 원본 손실을 방지합니다.
-   **상세 로그**: 터미널에 각 파일의 처리 과정, 성공/실패 여부, 최종 요약 정보를 출력합니다.

## 폴더 구조

```
/프로젝트_폴더
|
|-- input/
|   |-- (여기에 PDF 파일들을 넣으세요)
|   `-- .gitkeep
|
|-- output/
|   |-- (변환 결과 폴더들이 여기에 생성됩니다)
|   `-- .gitkeep
|
|-- your_script_name.py  (실행할 파이썬 스크립트)
|-- README.md            (현재 파일)
`-- .gitignore           (Git 버전 관리 제외 파일 목록)
```

## 사전 준비 (Prerequisites)

스크립트를 실행하기 위해 다음 프로그램 및 라이브러리가 설치되어 있어야 합니다.

1.  **Python 3**: [공식 웹사이트](https://www.python.org/)에서 다운로드 및 설치
2.  **Poppler**: PDF 렌더링을 위한 필수 도구입니다.
    -   **Windows**: [여기](https://github.com/oschwartz10612/poppler-windows/releases/)에서 최신 버전을 다운로드하여 압축을 푼 후, 내부의 `bin` 폴더 경로를 복사하여 스크립트의 `POPPLE_PATH_CONFIG` 변수에 설정해야 합니다.
        (윈도우는 기본으로 설정을 했습니다. 설치안해도 괜찮습니다.)
    -   **macOS (Homebrew)**: `brew install poppler`
    -   **Linux (apt)**: `sudo apt-get install poppler-utils`
3.  **파이썬 라이브러리**: 터미널에서 아래 명령어로 설치합니다.
    ```bash
    pip install pdf2image Pillow
    ```

## 사용 방법

1.  이 프로젝트를 다운로드하거나 복제합니다.
2.  `input` 폴더에 변환하고 싶은 PDF 파일들을 넣습니다.
3.  파이썬 스크립트(`your_script_name.py`)를 열어 `POPPLE_PATH_CONFIG` 변수에 자신의 Poppler `bin` 폴더 경로를 올바르게 설정합니다.
4.  터미널을 열고 아래 명령어로 스크립트를 실행합니다.
    ```bash
    python your_script_name.py
    ```
5.  작업이 완료되면 `output` 폴더에서 결과를 확인합니다.
