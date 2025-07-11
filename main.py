from medical_data_visualizer import draw_cat_plot, draw_heat_map
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Draw and save the categorical plot
    cat_fig = draw_cat_plot()
    cat_fig.savefig('catplot.png')
    plt.close(cat_fig)

    # Draw and save the heatmap
    heat_fig = draw_heat_map()
    heat_fig.savefig('heatmap.png')
    plt.close(heat_fig)

    print("Plots saved as 'catplot.png' and 'heatmap.png'")
