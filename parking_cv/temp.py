import numpy as np

# 442, 247

box1 = np.array([(162, 616), (79, 609), (0, 720), (75, 769)])
box2 = np.array([(300, 631), (187, 622), (91, 774), (208, 790)])
box3 = np.array([(451, 652), (328, 634), (231, 796), (361, 814)])
box4 = np.array([(610, 651), (480, 643), (391, 819), (553, 841)])
box5 = np.array([(783, 658), (639, 651), (586, 838), (769, 850)])
box6 = np.array([(970, 667), (820, 661), (804, 841), (976, 846)])
box7 = np.array([(1143, 673), (1006, 667), (1008, 858), (1171, 862)])
box8 = np.array([(1302, 678), (1176, 672), (1206, 858), (1374, 858)])
box9 = np.array([(1443, 673), (1330, 676), (1401, 853), (1545, 861)])
box10 = np.array([(1579, 676), (1477, 678), (1566, 855), (1680, 837)])
box11 = np.array([(1693, 667), (1599, 675), (1696, 831), (1797, 817)])
boxes = [box1, box2, box3, box4, box5, box6, box7, box8, box9, box10, box11]

i = 1
for box in boxes:
    #x = x, and 360 = y
    x = 455
    y = 255
    box[0] = (((int)((box[0][0] / 1920) * x)+10), (int)((box[0][1] / 1080) * y))
    box[1] = (((int)((box[1][0] / 1920) * x)+10), (int)((box[1][1] / 1080) * y))
    box[2] = (((int)((box[2][0] / 1920) * x)+10), (int)((box[2][1] / 1080) * y))
    box[3] = (((int)((box[3][0] / 1920) * x)+10), (int)((box[3][1] / 1080) * y))
    
    print(f"box{i} = np.array ([({box[0][0]}, {box[0][1]}), ({box[1][0]}, {box[1][1]}), ({box[2][0]}, {box[2][1]}), ({box[3][0]}, {box[3][1]})])")
    i += 1