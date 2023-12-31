import argparse
import json
import os
import sys

import supervisely as sly
from dataset_tools import ProjectRepo
from dotenv import load_dotenv

import src.options as o
import src.settings as s
from src.convert import convert_and_upload_supervisely_project

PARENT_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
LOCAL_ENV = os.path.join(PARENT_PATH, "local.env")
load_dotenv(os.path.expanduser("~/ninja.env"))
load_dotenv(LOCAL_ENV)
SERVER_ADDRESS = os.getenv("SERVER_ADDRESS")
TEAM_ID = sly.env.team_id()
WORKSPACE_ID = sly.env.workspace_id()


def get_project_info(api: sly.Api):
    s.check_names()

    project_info = api.project.get_info_by_name(WORKSPACE_ID, s.PROJECT_NAME)
    if not project_info:
        # If project doesn't found on instance, create it and use new project info.
        sly.logger.info(f"Project {s.PROJECT_NAME} not found on instance. Creating a new one...")
        project_info = convert_and_upload_supervisely_project(api, WORKSPACE_ID, s.PROJECT_NAME)
        sly.logger.info("Now you can explore created project and choose 'preview_image_id'.")
        sys.exit(0)
    else:
        sly.logger.info(f"Found project {s.PROJECT_NAME} on instance, will use it.")

    return project_info


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload dataset to instance.")
    parser.add_argument(
        "--forces", type=json.loads, default="{}", help="Which parameters to force."
    )

    args = parser.parse_args()
    forces = args.forces

    sly.logger.info(f"Script is starting with forces: {forces}")

    sly.fs.mkdir("./stats")
    sly.fs.mkdir("./visualizations")

    api = sly.Api.from_env()
    sly.logger.info(
        f"Connected to Supervisely. Server address: {SERVER_ADDRESS}, team_id: {TEAM_ID}, workspace_id: {WORKSPACE_ID}."
    )
    project_id = get_project_info(api).id
    settings = s.get_settings()

    stat_options = o.get_stats_options()
    vis_options = o.get_visualization_options()

    sly.logger.info(f"Starting to work with project id: {project_id}.")

    force_stats = forces.get("force_stats")
    force_visuals = forces.get("force_visuals")
import argparse
import json
import os
import sys

import supervisely as sly
from dataset_tools import ProjectRepo
from dotenv import load_dotenv

import src.options as o
import src.settings as s
from src.convert import convert_and_upload_supervisely_project

PARENT_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
LOCAL_ENV = os.path.join(PARENT_PATH, "local.env")
load_dotenv(os.path.expanduser("~/ninja.env"))
load_dotenv(LOCAL_ENV)
SERVER_ADDRESS = os.getenv("SERVER_ADDRESS")
TEAM_ID = sly.env.team_id()
WORKSPACE_ID = sly.env.workspace_id()


def get_project_info(api: sly.Api):
    s.check_names()

    project_info = api.project.get_info_by_name(WORKSPACE_ID, s.PROJECT_NAME)
    if not project_info:
        # If project doesn't found on instance, create it and use new project info.
        sly.logger.info(f"Project {s.PROJECT_NAME} not found on instance. Creating a new one...")
        project_info = convert_and_upload_supervisely_project(api, WORKSPACE_ID, s.PROJECT_NAME)
        sly.logger.info("Now you can explore created project and choose 'preview_image_id'.")
        sys.exit(0)
    else:
        sly.logger.info(f"Found project {s.PROJECT_NAME} on instance, will use it.")

    return project_info


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload dataset to instance.")
    parser.add_argument(
        "--forces", type=json.loads, default="{}", help="Which parameters to force."
    )

    args = parser.parse_args()
    forces = args.forces

    sly.logger.info(f"Script is starting with forces: {forces}")

    sly.fs.mkdir("./stats")
    sly.fs.mkdir("./visualizations")

    api = sly.Api.from_env()
    sly.logger.info(
        f"Connected to Supervisely. Server address: {SERVER_ADDRESS}, team_id: {TEAM_ID}, workspace_id: {WORKSPACE_ID}."
    )
    project_id = get_project_info(api).id
    settings = s.get_settings()

    stat_options = o.get_stats_options()
    vis_options = o.get_visualization_options()

    sly.logger.info(f"Starting to work with project id: {project_id}.")

    force_stats = forces.get("force_stats")
    force_visuals = forces.get("force_visuals")
import argparse
import json
import os
import sys

import supervisely as sly
from dataset_tools import ProjectRepo
from dotenv import load_dotenv

import src.options as o
import src.settings as s
from src.convert import convert_and_upload_supervisely_project

PARENT_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
LOCAL_ENV = os.path.join(PARENT_PATH, "local.env")
load_dotenv(os.path.expanduser("~/ninja.env"))
load_dotenv(LOCAL_ENV)
SERVER_ADDRESS = os.getenv("SERVER_ADDRESS")
TEAM_ID = sly.env.team_id()
WORKSPACE_ID = sly.env.workspace_id()


def get_project_info(api: sly.Api):
    s.check_names()

    project_info = api.project.get_info_by_name(WORKSPACE_ID, s.PROJECT_NAME)
    if not project_info:
        # If project doesn't found on instance, create it and use new project info.
        sly.logger.info(f"Project {s.PROJECT_NAME} not found on instance. Creating a new one...")
        project_info = convert_and_upload_supervisely_project(api, WORKSPACE_ID, s.PROJECT_NAME)
        sly.logger.info("Now you can explore created project and choose 'preview_image_id'.")
        sys.exit(0)
    else:
        sly.logger.info(f"Found project {s.PROJECT_NAME} on instance, will use it.")

    return project_info


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload dataset to instance.")
    parser.add_argument(
        "--forces", type=json.loads, default="{}", help="Which parameters to force."
    )

    args = parser.parse_args()
    forces = args.forces

    sly.logger.info(f"Script is starting with forces: {forces}")

    sly.fs.mkdir("./stats")
    sly.fs.mkdir("./visualizations")

    api = sly.Api.from_env()
    sly.logger.info(
        f"Connected to Supervisely. Server address: {SERVER_ADDRESS}, team_id: {TEAM_ID}, workspace_id: {WORKSPACE_ID}."
    )
    project_id = get_project_info(api).id
    settings = s.get_settings()

    stat_options = o.get_stats_options()
    vis_options = o.get_visualization_options()

    sly.logger.info(f"Starting to work with project id: {project_id}.")

    force_stats = forces.get("force_stats")
    force_visuals = forces.get("force_visuals")
import json
import os

from dotenv import load_dotenv

import dataset_tools as dtools
import supervisely as sly

if sly.is_development():
    load_dotenv(os.path.expanduser("~/ninja.env"))
    load_dotenv("local.env")

os.makedirs("./stats/", exist_ok=True)
os.makedirs("./visualizations/", exist_ok=True)
api = sly.Api.from_env()


# 1a initialize sly api way
project_id = sly.env.project_id()
project_meta = sly.ProjectMeta.from_json(api.project.get_meta(project_id))
datasets = api.dataset.get_list(project_id)


# 1b initialize sly localdir way
# project_path = os.environ["LOCAL_DATA_DIR"]
# sly.download(api, project_id, project_path, save_image_info=True, save_images=False)
# project_meta = sly.Project(project_path, sly.OpenMode.READ).meta
# datasets = None


project_info = api.project.get_info_by_id(project_id)
custom_data = project_info.custom_data

# 2. get download link
download_sly_url = dtools.prepare_download_link(project_info)
dtools.update_sly_url_dict({project_id: download_sly_url})


# 3. upload custom data
if len(custom_data) > 0:
    # preset fields
    custom_data = {
        # required fields
        "name": "PASCAL VOC 2012",
        "fullname": "PASCAL Visual Object Classes Challenge",
        "cv_tasks": [
            "semantic segmentation",
            "object detection",
            "instance segmentation",
        ],
        "annotation_types": ["instance segmentation"],
        "industries": ["general domain"],
        "release_year": 2012,
        "homepage_url": "http://host.robots.ox.ac.uk/pascal/VOC/voc2012/index.html",
        "license": "custom",
        "license_url": "http://host.robots.ox.ac.uk/pascal/VOC/voc2012/index.html#rights",
        "preview_image_id": 49551,
        "github_url": "https://github.com/dataset-ninja/pascal-voc-2012",
        "citation_url": "http://host.robots.ox.ac.uk/pascal/VOC/voc2012/index.html#citation",
        "download_sly_url": download_sly_url,
        # optional fields
        "download_original_url": "http://host.robots.ox.ac.uk/pascal/VOC/voc2012/index.html#devkit",
        "paper": "http://host.robots.ox.ac.uk/pascal/VOC/pubs/everingham15.pdf",
        # "organization_name": None,
        # "organization_url": None,
        # "tags": [],
    }
    api.project.update_custom_data(project_id, custom_data)


def build_stats():
    stats = [
        dtools.ClassBalance(project_meta),
        dtools.ClassCooccurrence(project_meta, force=False),
        dtools.ClassesPerImage(project_meta, datasets),
        dtools.ObjectsDistribution(project_meta),
        dtools.ObjectSizes(project_meta),
        dtools.ClassSizes(project_meta),
    ]
    heatmaps = dtools.ClassesHeatmaps(project_meta)
    classes_previews = dtools.ClassesPreview(
        project_meta, project_info.name, force=False
    )

    for stat in stats:
        if not sly.fs.file_exists(f"./stats/{stat.basename_stem}.json"):
            stat.force = True
    stats = [stat for stat in stats if stat.force]

    if not sly.fs.file_exists(f"./stats/{heatmaps.basename_stem}.png"):
        heatmaps.force = True
    if not sly.fs.file_exists(
        f"./visualizations/{classes_previews.basename_stem}.webm"
    ):
        classes_previews.force = True
    vstats = [stat for stat in [heatmaps, classes_previews] if stat.force]

    dtools.count_stats(
        project_id,
        stats=stats + vstats,
        sample_rate=1,
    )

    print("Saving stats...")
    for stat in stats:
        with open(f"./stats/{stat.basename_stem}.json", "w") as f:
            json.dump(stat.to_json(), f)
        stat.to_image(f"./stats/{stat.basename_stem}.png")

    if len(vstats) > 0:
        if heatmaps.force:
            heatmaps.to_image(
                f"./stats/{heatmaps.basename_stem}.png", draw_style="outside_black"
            )
        if classes_previews.force:
            classes_previews.animate(
                f"./visualizations/{classes_previews.basename_stem}.webm"
            )

    print("Stats done")


def build_visualizations():
    renderers = [
        dtools.Poster(project_id, project_meta, force=False),
        dtools.SideAnnotationsGrid(project_id, project_meta),
    ]
    animators = [
        dtools.HorizontalGrid(project_id, project_meta),
        dtools.VerticalGrid(project_id, project_meta, force=False),
    ]

    for vis in renderers + animators:
        if not sly.fs.file_exists(f"./visualizations/{vis.basename_stem}.png"):
            vis.force = True
    renderers, animators = [r for r in renderers if r.force], [
        a for a in animators if a.force
    ]

    for a in animators:
        if not sly.fs.file_exists(f"./visualizations/{a.basename_stem}.webm"):
            a.force = True
    animators = [a for a in animators if a.force]

    # Download fonts from https://fonts.google.com/specimen/Fira+Sans
    dtools.prepare_renders(
        project_id,
        renderers=renderers + animators,
        sample_cnt=40,
    )
    print("Saving visualization results...")
    for vis in renderers + animators:
        vis.to_image(f"./visualizations/{vis.basename_stem}.png")
    for a in animators:
        a.animate(f"./visualizations/{a.basename_stem}.webm")
    print("Visualizations done")


def build_summary():
    print("Building summary...")
    summary_data = dtools.get_summary_data_sly(project_info)

    if sly.fs.file_exists("./visualizations/classes_preview.webm"):
        classes_preview = (
            f"{custom_data['github_url']}/raw/main/visualizations/classes_preview.webm"
        )

    summary_content = dtools.generate_summary_content(
        summary_data,
        vis_url=classes_preview,
    )

    with open("SUMMARY.md", "w") as summary_file:
        summary_file.write(summary_content)
    print("Done.")


def main():
    pass
    # build_stats()
    # build_visualizations()
    # build_summary()


if __name__ == "__main__":
    main()
forces.get("force_texts")

    settings['force_texts'] = force_texts
    project_repo = ProjectRepo(api, project_id, settings)
    project_repo.build_stats(force=force_stats, settings=stat_options)
    project_repo.build_visualizations(force=force_visuals, settings=vis_options)

    project_repo.build_demo(force=force_demo)
    project_repo.build_demo(force=force_demo)
    project_repo.build_demo(force=force_demo)
    project_repo.build_texts(force=force_texts, preview_class=o.PREVIEW_CLASS)

    sly.logger.info("Script finished.")
forces.get("force_texts")

    settings['force_texts'] = force_texts
    project_repo = ProjectRepo(api, project_id, settings)
    project_repo.build_stats(force=force_stats, settings=stat_options)
    project_repo.build_visualizations(force=force_visuals, settings=vis_options)

    project_repo.build_demo(force=force_demo)
    project_repo.build_demo(force=force_demo)
    project_repo.build_texts(force=force_texts, preview_class=o.PREVIEW_CLASS)

    sly.logger.info("Script finished.")
forces.get("force_texts")

    settings['force_texts'] = force_texts
    project_repo = ProjectRepo(api, project_id, settings)
    project_repo.build_stats(force=force_stats, settings=stat_options)
    project_repo.build_visualizations(force=force_visuals, settings=vis_options)

    project_repo.build_demo(force=force_demo)
    project_repo.build_texts(force=force_texts, preview_class=o.PREVIEW_CLASS)

    sly.logger.info("Script finished.")
