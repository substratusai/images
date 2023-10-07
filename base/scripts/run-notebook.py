#!/usr/bin/env python3

import argparse
import sys
from pathlib import Path
import logging
import papermill
from papermill.log import logger
from papermill.engines import NBClientEngine, papermill_engines, NotebookExecutionManager, PapermillNotebookClient
from papermill.utils import merge_kwargs, remove_args
from nbconvert import HTMLExporter


parser = argparse.ArgumentParser(
    prog='run-notebook.py',
    description='Run a notebook and converts it to HTML while it is running')

parser.add_argument('notebook_path', help="The path to the .ipynb notebook file")
parser.add_argument('notebook_output_path', help="The path where the .ipynb notebook file should be written")
parser.add_argument('-c', '--cwd', help="Change the working directory")
args = parser.parse_args()

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger.setLevel(logging.INFO)

class HTMLExecutionManager(NotebookExecutionManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.html_exporter = HTMLExporter()
        self.html_output_path = Path(self.output_path).with_suffix(".html")

    def save(self, **kwargs):
        super().save(**kwargs)
        html_output, _ = self.html_exporter.from_notebook_node(self.nb)
        with self.html_output_path.open("w", encoding ="utf-8") as f:
            f.write(html_output)

class HTMLEngine(NBClientEngine):
    @classmethod
    def execute_notebook(
        cls,
        nb,
        kernel_name,
        output_path=None,
        progress_bar=True,
        log_output=False,
        autosave_cell_every=5,
        **kwargs,
    ):
        """
        A wrapper to handle notebook execution tasks.

        Wraps the notebook object in a `NotebookExecutionManager` in order to track
        execution state in a uniform manner. This is meant to help simplify
        engine implementations. This allows a developer to just focus on
        iterating and executing the cell contents.
        """
        nb_man = HTMLExecutionManager(
            nb,
            output_path=output_path,
            progress_bar=progress_bar,
            log_output=log_output,
            autosave_cell_every=autosave_cell_every,
        )

        nb_man.notebook_start()
        try:
            cls.execute_managed_notebook(nb_man, kernel_name, log_output=log_output, **kwargs)
        finally:
            nb_man.cleanup_pbar()
            nb_man.notebook_complete()

        return nb_man.nb


papermill_engines.register('htmlengine', HTMLEngine)
papermill_engines.register_entry_points()


# Execute the notebook with papermill as usual
papermill.execute_notebook(
    args.notebook_path,
    args.notebook_output_path,
    cwd=args.cwd,
    log_output=True,
    engine_name="htmlengine",
)