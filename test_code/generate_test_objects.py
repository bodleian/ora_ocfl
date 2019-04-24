#! /usr/bin/python3
"""
  generate_test_objects.py

  A test of the OCFL code libraries requires a decent sized repository for
  scale. This code generates a large number of objects into a root file system.

  Configuration options:

    OBJECTS_TO_CREATE (int): the number of objects you want to create inside
        the OCFL storage root
    OCFL_ROOT_PARENT_DIRECTORY (str): the path of the directory in which
        to create the new storage root
    TEST_CONTENT_DIRECTORY (str): directory containing sample files to
        add to the newly created test objects.

  This code will put objects into a pair-tree sub directory on the basis of
  their uuid.
"""

import os
import sys
import datetime
import subprocess
import time
import uuid


# Constants
OBJECTS_TO_CREATE = 1
OCFL_ROOT_PARENT_DIRECTORY = "/mnt/hard_disk/ocfl/test_roots"
TEST_CONTENT_DIRECTORY = ("/home/lina0911/code/ora4/repos/ora_data_model"
                          "/OCFL/test_code/test_object_content/")

OCFL_ROOT_PARENT_DIRECTORY = ("/home/lina0911/code/ora4/repos/ora_data_model"
                          "/OCFL/storage_root/")

def generate_path(uuid):
    """ Generate a pairtree path

    args:
      uuid (str): uuid of the object for which the path is being generated
    """
    # get first eight characters of the UUID
    first_eight_characters = uuid[0:8]
    directory_tree = list()

    # split first eight characters into a directory tree
    # with each part two characters long
    for i in range(0, len(first_eight_characters), 2):
        directory_tree.append(first_eight_characters[i:i+2])

    # Form the pair tree path
    pair_tree_path = '/'.join(directory_tree)
    return pair_tree_path


def generate_object(uuid=None, ocfl_root=None):
    """ Generate an OCFL object with a given UUID

    args:
      uuid (str): uuid of the object to generate
      ocfl_root (str): directory holding the OCFL storage root
    """
    pair_tree_path = generate_path(uuid)
    content_directory = TEST_CONTENT_DIRECTORY
    new_object_directory = os.path.join(ocfl_root, uuid)
    pair_tree_object_directory = os.path.join(ocfl_root, pair_tree_path)

    create_object_command = [
        "ocfl", "--root", ocfl_root, "cp", "-r", content_directory, uuid]
    make_child_directory = [
        "mkdir", "-p", pair_tree_object_directory]
    move_finished_directory = [
        "mv", new_object_directory, pair_tree_object_directory]

    print("Creating {}".format(uuid))
    subprocess.run(args=create_object_command)
    subprocess.run(args=make_child_directory)
    subprocess.run(args=move_finished_directory)


def create_objects(number_to_generate, ocfl_root=OCFL_ROOT_PARENT_DIRECTORY):
    """ Create a set of test objects in the OCFL storage root

    args:
      number_to_generate (int): number of objects to create
      ocfl_root (str): directory holding the OCFL storage root
    """
    for _ in range(0, int(number_to_generate)):
        fake_uuid = str(uuid.uuid4())
        generate_object(uuid=fake_uuid, ocfl_root=ocfl_root)


def create_ocfl_root(parent_directory=OCFL_ROOT_PARENT_DIRECTORY):
    """ Create an OCFL root in a given directory

    args:
      parent_directory (str): the path to the parent directory
          in which the OCFL storage root will be created.
    """
    timestamp = "{:%Y%m%d%H%m%S}".format(datetime.datetime.now())
    ocfl_root_directory = os.path.join(parent_directory, timestamp)

    try:
        os.mkdir(ocfl_root_directory)
    except FileExistsError:
        pass

    initiate_repo_command = ["ocfl", "mkroot", ocfl_root_directory]
    subprocess.run(args=initiate_repo_command)

    return ocfl_root_directory


def main():
    # Create the new test root directory and create the objects
    ocfl_root = create_ocfl_root(
        parent_directory=OCFL_ROOT_PARENT_DIRECTORY)
    print("Creating root directory at: {}".format(ocfl_root))
    create_objects(OBJECTS_TO_CREATE, ocfl_root)


if __name__ == "__main__":
    main()
