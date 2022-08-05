
import cv2


def delta_images(t0, t1, t2):
    d1 = cv2.absdiff(t2, t0)
    return d1


def motion_detection(t_minus, t_now, t_plus,screen):
    delta_view = delta_images(t_minus, t_now, t_plus)
    retval, delta_view = cv2.threshold(delta_view, 16, 255, 3)
    cv2.normalize(delta_view, delta_view, 0, 255, cv2.NORM_MINMAX)
    img_count_view = cv2.cvtColor(delta_view, cv2.COLOR_RGB2GRAY)
    delta_count = cv2.countNonZero(img_count_view)
    dst = cv2.addWeighted(screen,1.0, delta_view,0.6,0)
    delta_count_last = delta_count
    return delta_count