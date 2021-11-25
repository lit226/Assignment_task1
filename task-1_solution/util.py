import json
from PIL import Image
import  matplotlib.pyplot as plt
from matplotlib import patches
import sys
     
    
def Visualize_images(img_path,json_path,opacity=0.15):
    with open(json_path) as f:
        data = json.load(f)
    img = Image.open(img_path)
    fig = plt.figure(figsize = (30,12))
    plt.subplot(121)
    ax = fig.add_axes([0,0,1,1])
    plt.imshow(img)
    for i in range(1,len(data)-1):
        width = data[i]['original_width']
        height =data[i]['original_height']
        x_min = sys.maxsize
        x_max = -sys.maxsize
        y_min=sys.maxsize
        y_max = -sys.maxsize
        for x,y in data[i]['value']['points']:
            rx = (x*width)/100
            ry = (y*height)/100
            if(x_min > rx):
                x_min = rx
            if(x_max < rx):
                x_max = rx
            if(y_min > ry):
                y_min = ry
            if(y_max < ry):
                y_max= ry
        l = x_max- x_min
        b = y_max - y_min
        rect = patches.Rectangle((x_min,y_min), l, b, edgecolor = 'r', facecolor = 'none')
        ax.add_patch(rect)
       
    
    facecolor_val = [(1,1,0,opacity),(0,1,0,opacity),(1,0,1,opacity),(0,0,1,opacity),(1,0,0,opacity),(1,1,1,opacity)]
    fig = plt.figure(figsize = (30,12))
    plt.subplot(122)
    ax = fig.add_axes([0,0,1,1])
    plt.imshow(img)
    j=0
    for i in range(1,len(data)-1):
        width = data[i]['original_width']
        height =data[i]['original_height']
        x_min = 999999
        x_max = 0
        y_min=999999
        y_max = 0
        for x,y in data[i]['value']['points']:
            rx = (x*width)/100
            ry = (y*height)/100
            if(x_min > rx):
                x_min = rx
            if(x_max < rx):
                x_max = rx
            if(y_min > ry):
                y_min = ry
            if(y_max < ry):
                y_max= ry
        l = x_max- x_min
        b = y_max - y_min
        if j <6:
            rect = patches.Rectangle((x_min,y_min), l, b, edgecolor = 'w', facecolor = facecolor_val[j],label='Label')
        else:
            j=0
            rect = patches.Rectangle((x_min,y_min), l, b, edgecolor = 'w', facecolor = facecolor_val[j],label='Label')
            
        j+=1
        
        centerx =x_min
        centery = y_min
        plt.text(centerx, centery,"".join(data[i]['value']['polygonlabels']),color = 'r',ha='left',va = 'top',size=25)
        ax.add_patch(rect)