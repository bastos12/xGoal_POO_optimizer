COLUMNS_ENCODE = [
    'location',
    'bodypart',
    'assist_method',
    'situation'
    ]
ENCODED_COLUMNS = [
    'fast_break',
    'loc_centre_box',
    'loc_diff_angle_lr',
    'diff_angle_left',
    'diff_angle_right',
    'left_side_box',
    'left_side_6ybox',
    'right_side_box',
    'right_side_6ybox',
    'close_range',
    'penalty',
    'outside_box',
    'long_range',
    'more_35y',
    'more_40y',
    'not_recorded',
    'right_foot', 
    'left_foot',
    'header',
    'no_assist',
    'assist_pass',
    'assist_cross',
    'assist_header',
    'assist_through_ball',
    'open_play',
    'set_piece',
    'corner',
    'free_kick'
    ]

class Color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'