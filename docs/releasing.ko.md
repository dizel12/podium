# podium 버전 배포

[English](releasing.md)

## 브랜치와 배포 경로

`main`을 통합 브랜치로 유지합니다. 변경마다 짧게 쓰는 작업 브랜치를 만들고, PR에서 검사·검토 후 병합하고 브랜치를 삭제합니다. 외부 기여자는 이 저장소의 쓰기 권한 없이 자기 fork에서 작업할 수 있습니다.

`main`의 마켓플레이스 목록은 `github` 소스의 태그(`ref`)와 전체 커밋 SHA(`sha`)로 배포본 하나를 지정합니다. Claude Code는 둘 다 있으면 SHA를 사용합니다. 태그와 SHA는 같은 커밋을 가리켜야 합니다. 목록의 소스 지정을 바꾸기 전까지 `main`의 개발 커밋은 이 목록이 설치하는 플러그인을 바꾸지 않습니다.

플러그인 버전은 지정한 커밋의 `.claude-plugin/plugin.json`에 둡니다. 마켓플레이스 항목에 중복해서 적지 않습니다. 기존 설치는 이 버전으로 업데이트를 판단하므로, 소스 커밋만 바꾸고 같은 버전을 유지하는 것은 배포가 아닙니다.

## 새 버전 배포

1. 작업 브랜치에서 배포할 변경을 끝내고 `plugin.json`을 새 버전으로 올립니다. 사용자 파일의 영어·한국어를 맞추고 검사·검토 후 병합합니다.
2. 로컬 checkout에서 `claude --plugin-dir .`로 후보를 시험합니다. 마켓플레이스 설치는 의도적으로 이전 배포본을 선택합니다. `python3 scripts/ci/check_structure.py`, `claude plugin validate .`를 실행하고 실제 세션에서 바뀐 동작을 확인하며 남은 한계를 적습니다.
3. 시험한 커밋에 `vX.Y.Z` 태그를 만들고 push합니다. 그 커밋의 `plugin.json`은 `X.Y.Z`여야 합니다. 공개한 태그를 옮기거나 같은 배포 버전을 다른 내용에 재사용하지 않습니다.
4. 별도 목록 변경 PR에서 `source.ref`를 해당 태그로, `source.sha`를 전체 커밋 SHA로 바꿉니다. 태그와 SHA가 일치하고 지정한 manifest의 버전이 맞는지 확인합니다. 태그 안의 목록은 이전 배포본을 가리켜도 됩니다. 플러그인 설치는 해당 manifest를 읽으며 그 안의 목록을 다시 따라가지 않습니다. 태그 뒤에 목록을 갱신하면 자기 커밋 해시를 자신에게 적는 문제를 피합니다.
5. 검사 후 목록 PR을 병합하고 해당 태그의 GitHub Release 설명을 게시합니다. 변경점, 업그레이드 영향, 시험한 범위와 미확인 범위를 적습니다. 배포 대상은 목록의 소스 지정이 결정하고 GitHub Release는 이를 설명합니다.
6. 격리한 Claude Code 환경에서 신규 마켓플레이스 설치와 이전 버전의 업데이트를 확인합니다. 설치 버전과 실제 파일을 함께 확인합니다. 승인 없이 기존 사용자의 플러그인 설정을 바꿔 시험하지 않습니다.

`0.x` 단계의 버전 정책: 오류 수정은 patch, 의미 있는 기능·운영 흐름 변경은 minor를 올립니다. 호환성 변경은 명시합니다. 설정·파일 형식·문서화된 동작의 호환성을 안정적으로 약속할 때 `1.0.0`으로 올립니다. 배포하지 않는 커밋마다 버전을 올릴 필요는 없습니다.

## 업데이트와 로컬 개발

```bash
claude plugin marketplace update podium
claude plugin update podium@podium
```

사용자는 `/plugin` → Marketplaces에서 자동 업데이트를 켤 수 있습니다. 이 사용자 마켓플레이스가 자동으로 켜 주지는 않습니다. `stlahxm/podium#v0.1.0`처럼 특정 태그로 등록한 목록은 `main` 대신 그 태그에 고정됩니다.

개발 파일 시험은 checkout에서 `claude --plugin-dir .`를 사용합니다. 배포된 마켓플레이스 복사본 대신 로컬 파일을 읽습니다. 수정 후 다시 로드하거나 새 세션을 시작합니다. CLI 옵션과 동작은 설치한 Claude Code 버전에 따라 다르므로 공식 문서도 확인합니다.

## 공식 근거

- [목록 소스와 태그·커밋 지정](https://code.claude.com/docs/en/plugins/marketplace-reference)
- [버전 배포·업데이트 판단·자동 업데이트](https://code.claude.com/docs/en/plugins/host-marketplace)
- [플러그인 명령](https://code.claude.com/docs/en/plugins/cli-reference)
