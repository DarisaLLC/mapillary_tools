
from mapillary_tools.insert_MAPJson import insert_MAPJson


class Command:
    name = 'exif_insert'
    help = "Process unit tool : Format and insert Mapillary image description into image EXIF ImageDescription."

    def add_basic_arguments(self, parser):
        parser.add_argument(
            '--rerun', help='rerun the processing', action='store_true', required=False)
        parser.add_argument(
            '--skip_subfolders', help='Skip all subfolders and import only the images in the given directory path.', action='store_true', default=False, required=False)

    def add_advanced_arguments(self, parser):
        # master upload
        parser.add_argument('--master_upload', help='Process images with a master key, note: only used by Mapillary employees',
                            action='store_true', default=False, required=False)
        parser.add_argument('--skip_EXIF_insert', help='Skip inserting the extracted data into image EXIF.',
                            action='store_true', default=False, required=False)
        parser.add_argument('--keep_original', help='Do not overwrite original images, instead save the processed images in a new directory by adding suffix "_processed" to the import_path.',
                            action='store_true', default=False, required=False)

    def run(self, args):

        insert_MAPJson(**vars(args))
