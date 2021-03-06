PI = 3.14159265359
TAU = 2*PI

BOT_RADIUS = 1
BOT_DIAMETER = 2*BOT_RADIUS
WHEEL_RADIUS = .5

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
#Factor to scale our calculation output into the render canvas
#Directly proportional to how large our renders are
CANVAS_SCALE = 10

RENDER_BOT_RADIUS = CANVAS_SCALE*BOT_RADIUS
RENDER_HEAD_RADIUS = RENDER_BOT_RADIUS

THETA_MIN = 0
THETA_MAX = TAU
THETA_RANGE = abs(THETA_MAX-THETA_MIN)

TRACKER_DOT_STEP = 1
