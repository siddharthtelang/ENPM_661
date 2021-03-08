Siddharth Telang
stelang@umd.edu
116764520

ENPM 661 Planning for Autonomous Robots
Project 2

Folder contents:
1) BFS_point.py - main source file to run
2) map.jpg - map created using algebraic equations - serve as input for final video rendering
3) geogebra-export_Part1.ggb & geogebra-export_Part_2.ggb - exported map from geogebra
2) ReadMe.txt - this file - for instructions
3) sample_outputs/BFS_Final_Video.avi - video of node exploration - 0,0 to 399,299
4) sample_outputs/final_map.jpg - image file for node exploration - 0,0 to 399,299

Note: As I had created the map before extra dimension information was provided, this map has a very slight variation in coordinates
      of the hexagon

Geogebra guidelines:
https://www.geogebra.org/calculator
You may open this website to open the file mentioned in 3) to get the map.
This can be useful if you wish to test some points on the map

Final code guidelines:
1) Kindly make sure 'map.jpg' exists in the current folder
2) Run BFS_point.py  'python3 BFS_point.py'
3) It will ask for input coordinates - Enter the initial points - x coordinate followed by Enter and then y coordinate
   Same would be asked for final points.
4) If any of these coordinates lie in the obstacle region or outside boundary, the points will have to re-entered
   the code displays appropriate information.
5) When a valid set of points are provided, the script will run the algorithm and determine the path, printing all the nodes traversed
6) At the end of the execution, the video and final map will be saved in the current working directory
7) The nodes expolered will be shown in white color against black background ; while the final path would be highlighed in Green

Github Link:
https://github.com/siddharthtelang/ENPM_661/tree/main/Project2
