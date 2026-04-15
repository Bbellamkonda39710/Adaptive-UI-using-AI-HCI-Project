# Adaptive-UI-using-AI-HCI-Project

**Project Description**

Artificial intelligence application and human-computer interaction concepts were integrated to come up with an adaptive student recommendation system. A student performance dataset was used to generate recommendations. Cosine similarity and scaling of the features are implemented to find students who share a similar learning pattern and offer an adaptive user interface experiences depending on the performance.

**Features**

The system offers the following features: It recommends similar students, creates adaptive dashboards depending on the level of performance and has an interactive interface in the form of GUI using Tkinter, which allows easy navigation and better user experience.

**Dataset**

The dataset involved is an adaptive English learning dataset that has student performance attributes of reading speed, pronunciation accuracy, listening score, speaking score, level of engagement, adaptive score, and rate of improvement. Similarity among students is determined using these features.

**Technologies Used**

Data handling and preprocessing are done in Python and other libraries like Pandas and NumPy. MinMax scaling and computing the cosine similarity is done using scikit-learn, and Tkinter is used to create a graphical user interface.

**System Workflow**

The workflow starts with loading and cleaning the dataset, including the removal of additional spaces and processing of the data formatting. Categorical values are turned into numeric values and important features are selected. The data is then summed up into student profiles and normalized with MinMaxScaler. The cosine similarity is calculated to detect similar students and the system presents the recommendations and an adaptive dashboard according to the performance levels using a GUI.

**Sample Execution**

**Input: Enter Student ID: S101**

Output: Recommended Students:
S205
S309
S412

**Learning Outcomes**

The project assisted in comprehending the recommendation systems based on cosine similarity, methods of pre-processing data, and application of adaptive user interfaces based on the concepts of AI and HCI.

**Future Improvements**

The next step is to add more advanced models, improve the graphical interface and make the system a web-based application to ensure easier accessibility.



