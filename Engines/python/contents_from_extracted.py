import os
import shutil
import logging

from .lib.bins_update import bins_update
from .lib import pes_uniparam_edit as uniparamtool
from .lib.model_packing import models_pack
from .lib.cpk_tools import files_fetch_from_cpks
from .lib.utils.pausing import pause
from .lib.utils.logging_tools import logger_stop
from .lib.utils.FILE_INFO import (
    EXTRACTED_PATH,
    PATCHES_CONTENTS_PATH,
    BIN_FOLDER_PATH,
    TEAMCOLOR_BIN_NAME,
    UNICOLOR_BIN_NAME,
    UNIPARAM_NAME,
    UNIPARAM_18_NAME,
    UNIPARAM_19_NAME,
)


def contents_from_extracted():

    # Read the necessary parameters
    fox_mode = (int(os.environ.get('PES_VERSION', '19')) >= 18)
    fox_19 = (int(os.environ.get('PES_VERSION', '19')) >= 19)

    multicpk_mode = int(os.environ.get('MULTICPK_MODE', '0'))
    bins_updating = int(os.environ.get('BINS_UPDATING', '0'))


    # Set the name for the folders to put stuff into
    if not multicpk_mode:

        faces_foldername = "Singlecpk"
        uniform_foldername = "Singlecpk"
        bins_foldername = "Singlecpk"

    else:

        faces_foldername = "Facescpk"
        uniform_foldername = "Uniformcpk"
        bins_foldername = "Binscpk"


    # Create folders just in case
    os.makedirs(f"{PATCHES_CONTENTS_PATH}/{faces_foldername}", exist_ok=True)
    os.makedirs(f"{PATCHES_CONTENTS_PATH}/{uniform_foldername}", exist_ok=True)


    print("-")
    print("- Preparing the patch folders")
    print("-")


    # Put RefAppearance in CPK no matter what
    if not fox_mode:

        print("-")
        print("- Injecting 4cc referees files (pre-fox)")
        print("-")

        # Set the paths
        common_root_path = os.path.join(PATCHES_CONTENTS_PATH, bins_foldername, "common")
        refappearance_path = os.path.join(common_root_path, "character0", "model", "character", "appearance")
        refs_uniform_path = os.path.join(common_root_path, "character0", "model", "character", "uniform", "team", "referee")
        refs_clothes_path = os.path.join(common_root_path, "character0", "model", "character", "uniform", "nocloth")
        ng_socks_fix_path = os.path.join(common_root_path, "character1", "model", "character", "uniform", "nocloth")

        # Prepare a list of sources and destination paths for the bin files
        bins_folder_path = "Engines/bins/"

        refappearance_bin_path = os.path.join(bins_folder_path, "RefereeAppearance.bin")

        ref_acl_1_path = os.path.join(bins_folder_path, "referee_ACL_1.bin")
        ref_acl_2_path = os.path.join(bins_folder_path, "referee_ACL_2.bin")
        ref_acl_3_path = os.path.join(bins_folder_path, "referee_ACL_3.bin")
        ref_acl_4_path = os.path.join(bins_folder_path, "referee_ACL_4.bin")
        ref_acl_5_path = os.path.join(bins_folder_path, "referee_ACL_5.bin")
        ref_cl_1_path = os.path.join(bins_folder_path, "referee_CL_1.bin")
        ref_cl_2_path = os.path.join(bins_folder_path, "referee_CL_2.bin")
        ref_cl_3_path = os.path.join(bins_folder_path, "referee_CL_3.bin")
        ref_cl_4_path = os.path.join(bins_folder_path, "referee_CL_4.bin")
        ref_def_1_path = os.path.join(bins_folder_path, "referee_DEF_1.bin")
        ref_def_2_path = os.path.join(bins_folder_path, "referee_DEF_2.bin")
        ref_def_3_path = os.path.join(bins_folder_path, "referee_DEF_3.bin")
        ref_def_4_path = os.path.join(bins_folder_path, "referee_DEF_4.bin")
        ref_def_5_path = os.path.join(bins_folder_path, "referee_DEF_5.bin")
        ref_lb_1_path = os.path.join(bins_folder_path, "referee_LB_1.bin")
        ref_lb_2_path = os.path.join(bins_folder_path, "referee_LB_2.bin")
        ref_lb_3_path = os.path.join(bins_folder_path, "referee_LB_3.bin")
        ref_sda_1_path = os.path.join(bins_folder_path, "referee_SDA_1.bin")
        ref_sda_2_path = os.path.join(bins_folder_path, "referee_SDA_2.bin")
        ref_sda_3_path = os.path.join(bins_folder_path, "referee_SDA_3.bin")
        
        ref_collar_model_path = os.path.join(bins_folder_path, "referee_collar_026.model")
        ref_pants_model_path = os.path.join(bins_folder_path, "referee_pants_016.model")

        socks_no_guard_model_path = os.path.join(bins_folder_path, "socks_noguard.model")

        # Create the folders
        os.makedirs(refappearance_path, exist_ok=True)
        os.makedirs(refs_uniform_path, exist_ok=True)
        os.makedirs(refs_clothes_path, exist_ok=True)
        os.makedirs(ng_socks_fix_path, exist_ok=True)

        # And copy them to the Bins cpk folder
        shutil.copy(refappearance_bin_path, refappearance_path)

        shutil.copy(ref_acl_1_path, refs_uniform_path)
        shutil.copy(ref_acl_2_path, refs_uniform_path)
        shutil.copy(ref_acl_3_path, refs_uniform_path)
        shutil.copy(ref_acl_4_path, refs_uniform_path)
        shutil.copy(ref_acl_5_path, refs_uniform_path)
        shutil.copy(ref_cl_1_path, refs_uniform_path)
        shutil.copy(ref_cl_2_path, refs_uniform_path)
        shutil.copy(ref_cl_3_path, refs_uniform_path)
        shutil.copy(ref_cl_4_path, refs_uniform_path)
        shutil.copy(ref_def_1_path, refs_uniform_path)
        shutil.copy(ref_def_2_path, refs_uniform_path)
        shutil.copy(ref_def_3_path, refs_uniform_path)
        shutil.copy(ref_def_4_path, refs_uniform_path)
        shutil.copy(ref_def_5_path, refs_uniform_path)
        shutil.copy(ref_lb_1_path, refs_uniform_path)
        shutil.copy(ref_lb_2_path, refs_uniform_path)
        shutil.copy(ref_lb_3_path, refs_uniform_path)
        shutil.copy(ref_sda_1_path, refs_uniform_path)
        shutil.copy(ref_sda_2_path, refs_uniform_path)
        shutil.copy(ref_sda_3_path, refs_uniform_path)

        shutil.copy(ref_collar_model_path, refs_clothes_path)
        shutil.copy(ref_pants_model_path, refs_clothes_path)

        shutil.copy(socks_no_guard_model_path, ng_socks_fix_path)

    faces_folder_path = os.path.join("./patches_contents", faces_foldername)

    # Packing the face folders if 'Faces' directory exists
    main_dir = os.path.join(EXTRACTED_PATH, "Faces")
    if os.path.exists(main_dir):

        print("- \n- Packing the face folders")

        models_pack('face', main_dir, 'face/real', faces_folder_path)


    # Moving the kit configs if 'Kit Configs' directory exists
    main_dir = os.path.join(EXTRACTED_PATH, "Kit Configs")
    if os.path.exists(main_dir):
        print("- \n- Moving the kit configs")

        items_dir = f"{PATCHES_CONTENTS_PATH}/{uniform_foldername}/common/character0/model/character/uniform/team"

        # Create a "team" folder if needed
        os.makedirs(items_dir, exist_ok=True)

        # Move the kit configs to the Uniform cpk folder
        for item in os.listdir(main_dir):
            item_path = os.path.join(main_dir, item)
            target_item_path = os.path.join(items_dir, item)

            # If the target item path exists, remove it
            if os.path.exists(target_item_path):
                shutil.rmtree(target_item_path)

            # Move the item to the target directory
            shutil.move(item_path, items_dir)

        # Delete the main 'Kit Configs' folder
        if os.path.exists(main_dir):
            shutil.rmtree(main_dir)


    # If there's a Kit Textures folder, move its stuff
    main_dir = os.path.join(EXTRACTED_PATH, "Kit Textures")
    if os.path.exists(main_dir):
        print("- \n- Moving the kit textures")

        items_dir = (
            f"{PATCHES_CONTENTS_PATH}/{uniform_foldername}/common/character0/model/character/uniform/texture" if not fox_mode
            else f"{PATCHES_CONTENTS_PATH}/{uniform_foldername}/Asset/model/character/uniform/texture/#windx11"
        )

        # Create a texture folder if needed
        os.makedirs(items_dir, exist_ok=True)

        # Move the kit textures to the Uniform cpk folder
        for item in os.listdir(main_dir):
            item_path = os.path.join(main_dir, item)
            target_item_path = os.path.join(items_dir, item)

            # If the target item path exists, remove it
            if os.path.exists(target_item_path):
                os.remove(target_item_path)

            # Move the item to the target directory
            shutil.move(item_path, items_dir)

        # Delete the main 'Kit Textures' folder
        if os.path.exists(main_dir):
            shutil.rmtree(main_dir)


    # If there's a Boots folder, move or pack its stuff
    main_dir = os.path.join(EXTRACTED_PATH, "Boots")
    if os.path.exists(main_dir):

        if not fox_mode:
            print('-')
            print('- Moving the boots')
        else:
            print('-')
            print('- Packing the boots folders')

        models_pack('boots', main_dir, 'boots', faces_folder_path)

    # If there's a Gloves folder, move its stuff
    main_dir = os.path.join(EXTRACTED_PATH, "Gloves")
    if os.path.exists(main_dir):

        if not fox_mode:
            print('-')
            print('- Moving the gloves')
        else:
            print('-')
            print('- Packing the gloves folders')

        models_pack('glove', main_dir, 'glove', faces_folder_path)


    other_message = False

    # If there's a Collars folder, move its stuff
    main_dir = os.path.join(EXTRACTED_PATH, "Collars")
    if os.path.exists(main_dir):

        if not other_message:
            other_message = True

            print('-')
            print('- Moving the other stuff')

        items_folder_path = (
            'common/character0/model/character/uniform/nocloth' if not fox_mode
            else 'Asset/model/character/uniform/nocloth/#Win'
        )

        # Create a "collars" folder if needed
        items_folder_path_full = os.path.join(PATCHES_CONTENTS_PATH, faces_foldername, items_folder_path)
        if not os.path.exists(items_folder_path_full):
            os.makedirs(items_folder_path_full)

        # Move the collars to the Faces cpk folder
        for item in os.listdir(main_dir):
            shutil.move(os.path.join(main_dir, item), items_folder_path_full)

        # Then delete the main folder
        shutil.rmtree(main_dir)


    # Set the common folder path depending on the fox mode setting
    if not fox_mode:
        common_path = 'common/character1/model/character/uniform/common'
    else:
        common_path = 'Asset/model/character/common'

    # If there's a Common folder, move its stuff
    main_dir = os.path.join(EXTRACTED_PATH, 'Common')
    if os.path.exists(main_dir):

        if not other_message:
            other_message = True

            print('-')
            print('- Moving the other stuff')

        # Create a "common" folder if needed
        items_folder_path_full = os.path.join(PATCHES_CONTENTS_PATH, faces_foldername, common_path)
        if not os.path.exists(items_folder_path_full):
            os.makedirs(items_folder_path_full)

        # Move the team folders to the Faces cpk folder
        for item in os.listdir(main_dir):

            if not fox_mode:

                # If the folder already exists, delete it
                if os.path.exists(os.path.join(items_folder_path_full, item)):
                    shutil.rmtree(os.path.join(items_folder_path_full, item))

                # Move the folder
                shutil.move(os.path.join(main_dir, item), items_folder_path_full)

            else:

                # Create a team subfolder
                subfolder = os.path.join(items_folder_path_full, item, 'sourceimages/#windx11')
                if not os.path.exists(subfolder):
                    os.makedirs(subfolder)

                # Move the files inside the folder to the subfolder
                for subitem in os.listdir(os.path.join(main_dir, item)):
                    # First delete if it already exists
                    if os.path.exists(os.path.join(subfolder, subitem)):
                        os.remove(os.path.join(subfolder, subitem))

                    shutil.move(os.path.join(main_dir, item, subitem), subfolder)

        # Then delete the main folder
        shutil.rmtree(main_dir)


    # Finally delete the "extracted" folder
    if os.path.exists(EXTRACTED_PATH):
        shutil.rmtree(EXTRACTED_PATH)


    if 'all_in_one' in os.environ:

        print('-')
        print('- Patch contents folder prepared')
        print('-')

    else:

        print('-')
        print('- The patches_contents folder has been prepared')
        print('-')
        print('- 4cc aet compiler by Shakes')
        print('-')
