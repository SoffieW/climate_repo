import click
import dotenv
import os
import subprocess
from pathlib import Path 
import zipfile 

@click.command()
@click.argument('kaggle_api_path', type=click.Path())
def main(kaggle_api_path):
    """ Downloads data from kaggle into directory (../raw) using the Kaggle API. Ensure that .env is updated with
    KAGGLE_USERNAME and KAGGLE_KEY before running this script.
    """
    # Create Path object and create "new_folder" in current working directory (Path.cwd())
    output_path = Path(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir,"data", "raw"))
#output_path.mkdir()
# Specify the dataset you want to download
    project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir) # path to project dir
#output_path = os.path.join(project_dir, 'data', 'raw')
# Specify the directory where you want to download the dataset

# Download the dataset
    # Download datasets
    subprocess.run(["kaggle", "datasets", "download", "-d", kaggle_api_path, "-p", output_path])


    glob_obj = output_path.glob('*.zip')
    for i in glob_obj:
        zip_path = i

    zipdata = zipfile.ZipFile(zip_path)
    zipinfos = zipdata.infolist()

    for zipinfo in zipinfos:
        zipinfo.filename = "dataset.csv"
        zipdata.extract(zipinfo, output_path)

    print(f"Dataset extracted to {os.path.join(output_path, zipinfo.filename)}")
if __name__ == "__main__":
    main()



