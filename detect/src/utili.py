
from matplotlib import pyplot
from matplotlib.patches import Rectangle

def encoder_dic(valid_data):
    data_dic = {}
    (valid_boxes, valid_labels, valid_scores) = valid_data
    
    # Dictionary to keep only the highest score for each label
    highest_score_boxes = {}
    
    for box, label, score in zip(valid_boxes, valid_labels, valid_scores):
        # If the label is not in the dictionary or has a lower score, update it
        if label not in highest_score_boxes or score > highest_score_boxes[label][0]:
            highest_score_boxes[label] = (score, box)  # Update with higher score and box

    # Build the final dictionary with the "kept" status
    for label, (score, box) in highest_score_boxes.items():
        data_dic[label] = [[score, box, 'kept']]  # Keep only the highest scoring box

    return data_dic


def draw_boxes(filename, valid_data):

	data = pyplot.imread(filename)
	pyplot.imshow(data)
	ax = pyplot.gca()
	for i in range(len(valid_data[0])):
		box = valid_data[0][i]
		y1, x1, y2, x2 = box.ymin, box.xmin, box.ymax, box.xmax
		width, height = x2 - x1, y2 - y1
		rect = Rectangle((x1, y1), width, height, fill=False, color='white')
		ax.add_patch(rect)
		print(valid_data[1][i], valid_data[2][i])
		label = "%s (%.3f)" % (valid_data[1][i], valid_data[2][i])
		pyplot.text(x1, y1, label, color='white')
	pyplot.show()