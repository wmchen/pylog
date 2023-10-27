"""
Log management
Programmer: Weiming Chen
Copyright © 2023-present Weiming Chen. All rights reserved.
"""
import sys
from typing import Optional
from pathlib import Path
from loguru import logger

__all__ = ['init_logger']


_default_format = ('<green>{time:YYYY-MM-DD HH:mm:ss}</green>'
                   ' <red>|</red> <yellow>elapsed: {elapsed}</yellow>'
                   ' <red>|</red> <level>{level: <8}</level> <red>|</red>'
                   ' <cyan>{file}</cyan> <cyan>{module}</cyan><red>:</red><cyan>{function}</cyan>'
                   ' <red>[</red><cyan>{line}</cyan><red>]</red> <red>-</red> <level>{message}</level>')


def init_logger(log_path: str | Path = '',
                save_log_file: bool = True,
                form: Optional[str] = _default_format,
                **kwargs):
    """
    Initialize the logger
    Args
        log_path (str | Path): the path of log file, only be used when save_log_file=True
        save_log_file (bool): whether to save the log file, default is True
        form (optional, str): the format of logging output, default format is "_default_format"
    """
    logger.remove(handler_id=None)  # clear default settings
    logger.add(sys.stdout, format=form)  # set the logging output of console
    if save_log_file:
        assert log_path.endswith('.log') or log_path.suffix == '.log', 'The suffix of log file must be ".log"'
        log_path = Path(log_path)
        if not log_path.parent.exists():
            log_path.parent.mkdir(parents=True)
        logger.add(log_path, format=form, **kwargs)  # set the logging output of log file
    return logger
