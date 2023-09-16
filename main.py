from seam_carving import SeamCarver
import argparse
import os



def image_resize_without_mask(filename_input, filename_output, new_height, new_width):
    obj = SeamCarver(filename_input, new_height, new_width)
    obj.save_result(filename_output)


# def image_resize_with_mask(filename_input, filename_output, new_height, new_width, filename_mask):
#     obj = SeamCarver(filename_input, new_height, new_width, protect_mask=filename_mask)
#     obj.save_result(filename_output)


# def object_removal(filename_input, filename_output, filename_mask):
#     obj = SeamCarver(filename_input, 0, 0, object_mask=filename_mask)
#     obj.save_result(filename_output)



if __name__ == '__main__':

    ap = argparse.ArgumentParser()

    ap.add_argument("-im", help="Path to image", required=True)
    ap.add_argument("-out", help="Output file name", required=True)
    ap.add_argument("-nh", help="The height of the target image", type=int, required=True)
    ap.add_argument("-nw", help="The width of the target image", type=int, required=True)
    args = vars(ap.parse_args())

    IM_PATH, OUTPUT_NAME, TARGET_HEIGHT, TARGET_WIDTH = args["im"], args["out"], args["nh"], args["nw"]


    image_resize_without_mask(IM_PATH, OUTPUT_NAME, TARGET_HEIGHT, TARGET_WIDTH)
