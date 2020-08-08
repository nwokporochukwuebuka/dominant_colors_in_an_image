def dominant_colors_for_png_files(file_name, k):
    '''This function tells the dominant colors in a PNG file.'''
    
    # Import libraries
    import matplotlib.pyplot as plt
    import random
    import matplotlib.image as img
    import pandas as pd
    from scipy.cluster.vq import kmeans
    import seaborn as sns
    
    # Import Image
    image = img.imread(file_name)
    
    # Extracting the RGB values
    r = []; g = []; b = [];
    
    for row in image:
        for pixel in row:
            # A pixel contains RGB values 
            temp_r, temp_g, temp_b = pixel

            r.append(temp_r)
            g.append(temp_g)
            b.append(temp_b)
        
    # Putting the pixels into a dataframe
    pixels = pd.DataFrame({'red': r,  'green': g , 'blue': b})
    
    cluster_centers, _ = kmeans(pixels[['red', 'green',
                                    'blue']], k, iter=10)
    colors = []
    
    for cluster_center in cluster_centers:
        scaled_r, scaled_g, scaled_b = cluster_center

        colors.append((
        scaled_r,
        scaled_g ,
        scaled_b ))
    
    # Dimensions: 1 *  2 * 3 (1 * N * 3)
    plt.imshow([colors])
    return plt.show()
