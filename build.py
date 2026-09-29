#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""MemoTrace 打包入口 —— 项目唯一的启动文件。

为什么这个文件放在项目根目录（而不是 build_scripts/ 里）：
    Python 启动时会把「被执行的脚本所在目录」放进 sys.path[0]。
    入口脚本住在根目录，`build_scripts/` 与 `memotrace_version.py` 就天然可导入，
    因此 build_scripts/ 下的各脚本不需要任何 sys.path 操作代码，
    也不需要在当前环境里执行 pip install。

用法（在任意目录下都可以执行，不必先 cd）：
    python build.py                        # 交互式菜单
    python build.py --mode 1 -y            # 1=PyInstaller 2=Nuitka 3=cx_Freeze 4=全部
    python build.py --mode 4 -y --no-input # 完全非交互，适合 CI

等价写法（必须在项目根目录执行，无需本文件）：
    python -m build_scripts.pack_memotrace
"""

from build_scripts.pack_memotrace import MemoTraceMainPacker


def main():
    MemoTraceMainPacker().main()


if __name__ == "__main__":
    main()
