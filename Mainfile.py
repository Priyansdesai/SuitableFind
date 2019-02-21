class UpperDivision_Courses:  
	def __init__(self, code, name, keywords, prerequisites, description):
	    self.code = code
	    self.name = name
	    self.keywords = keywords
	    self.prerequisites = prerequisites
	    self.description = description
#_______________________________________________________________________________________________________________________________________________________________
class Student:
  def __init__(self, name):
    self.name = name
    self.courses_selected = []
    student_selections[self.name] = self.courses_selected
    self.schedule = {}
    self.final = {}
    self.pre_req = []
    self.lower_div = []
  #_______________________________________________________________________________________________________________________________________________________________
  def plan(self, starting_semester, starting_year, total_semesters):
  	if starting_semester == 'Fall' and total_semesters > 0:
  		self.schedule[('Fall', starting_year)] = []
  		Student.plan(self, 'Spring', (starting_year + 1), (total_semesters - 1))
  	elif starting_semester == 'Spring' and total_semesters > 0:
  		self.schedule[('Spring', starting_year)] = []
  		Student.plan(self, 'Fall', (starting_year), (total_semesters - 1))
  	else:
  		print(self.courses_selected)
  		for key, value in self.schedule.items():
  			print(key)
  			print('Enter the number of courses you want to take in this semester. Limit it to 2')
  			self.max = int(input())
  			for i in range(0, self.max):
  				self.add = str(input())
  				if self.add in tough_upperdivs and [f for f in value if f in tough_upperdivs]:
  					print('You are trying to add an uppder-division course that creates a tough combination with your existing combination')
  					print('Do you still wish to add it?')
  					answer = str(input())
  					if answer == 'Yes' or answer == 'yes' or answer == 'YES' or answer == 'Y' :
  						value.append(self.add)
  					else:
  						print(self.add,'has not been added to your final plan')
  				else:
  					value.append(self.add)
  		print(self.schedule)
  		print('Thank you for using EECS online services')
  #_______________________________________________________________________________________________________________________________________________________________
  def plan_a_schedule(self, courses):
  	print('------------------------------------------------------------------------------------------------------------------------------------------------------------------')
  	print('When do you want to start taking upper-division courses?')
  	print('Enter the year')
  	self.year_input = int(input())
  	print('Enter the semester')
  	self.semester = str(input())
  	print('------------------------------------------------------------------------------------------------------------------------------------------------------------------')
  	print('Enter the number of semesters you would continue taking upper-division courses until graduation')
  	self.total_semesters = int(input())
  	print('------------------------------------------------------------------------------------------------------------------------------------------------------------------')
  	Student.plan(self, self.semester, self.year_input, self.total_semesters)
  #_______________________________________________________________________________________________________________________________________________________________
  def preq_check(self, RequirementA, RequirementB, Courses):
  	for c in Courses:
  		self.in_case_no_completion = ['You need to still satisfy']
  		for p in dic[c].prerequisites:
  			if p in RequirementA or p in RequirementB:
  				self.final[c] = 'Yes' 
  			else:
  				if p == 'MATH54' and 'EE16A' in RequirementB and 'EE16A' in RequirementB:
  					self.final[c] = 'Yes'
  				elif (p == 'CS70' and 'MATH55' in RequirementB) or (p == 'MATH55' and 'CS70' in RequirementA):
  					self.final[c] = 'Yes'
  				else:
  					self.in_case_no_completion.append(p)
  					self.final[c] = self.in_case_no_completion
  	print('Your selection is:', self.final)
  	print('------------------------------------------------------------------------------------------------------------------------------------------------------------------')
  	print('Would you want to plan a schedule for this selection?')
  	second_input = str(input())
  	if second_input =='Yes' or second_input =='YES' or second_input =='Y' or second_input =='yes' :
  		Student.plan_a_schedule(self, self.courses_selected)
  	else:
  		print("Thank you for using SuitableFind's services")
  #_______________________________________________________________________________________________________________________________________________________________
  def select(self, course):
  	obj = dic[course]
  	self.courses_selected.append(obj.code)
  #_______________________________________________________________________________________________________________________________________________________________
  def input_know_more(self, number):
  	if self.courses_selected:
  		for c in [(dic[course].code, dic[course].description) for course in self.courses_selected]:
  			print (c)
  		print('------------------------------------------------------------------------------------------------------------------------------------------------------------------')
  		print('Now, would you want to run a prerequisites check')
  		a = str(input())
  		if a == 'Yes' or a == 'YES' or a == 'Y' or a == 'yes' :
  			Student.preq_check(self,self.pre_req, self.lower_div, self.courses_selected)
  	elif self.searched and number == len(self.searched):
  		for c in [(dic[course[0]].code, dic[course[0]].description) for course in self.searched]:
  			print(c)
  		print('------------------------------------------------------------------------------------------------------------------------------------------------------------------')
  		print('Now would you want to select your courses')
  		b = str(input())
  		if b == 'Yes' or b == 'YES' or b == 'Y' or b == 'yes' :
  			for c in self.searched:
  				Student.select(self, c[0])
  		Student.input_know_more(self, len(self.courses_selected))
  	else:
  		self.new = []
  		for i in range(0, number):
	  		self.ask = str(input())
	  		self.new.append([dic[self.ask].code, dic[self.ask].description])
	  	for c in self.new:
	  		print(c)
	  	print('------------------------------------------------------------------------------------------------------------------------------------------------------------------')
	  	print('Now would you want to select only the courses you wanted to know more about or all the courses that you searched')
	  	print('0) All of them.')
	  	print('1) Only ones I wanted to know more about')
	  	c = int(input())
	  	print('------------------------------------------------------------------------------------------------------------------------------------------------------------------')
	  	if c == 0:
	  		for d in self.searched:
  				Student.select(self, d[0])
  			Student.input_know_more(self, len(self.searched))
  		elif c == 1:
  			for d in self.new:
  				Student.select(self, d[0])
  			Student.input_know_more(self, len(self.new))
  #_______________________________________________________________________________________________________________________________________________________________
  def input_loop(self, select):
  	for i in range(0, select):
  		self.choose = str(input())
  		self.select(self.choose)
  	print('------------------------------------------------------------------------------------------------------------------------------------------------------------------')
  	print('The classes you have selected are:')
  	print(self.courses_selected)
  	print('------------------------------------------------------------------------------------------------------------------------------------------------------------------')
  	print('Do you want to check whether you satisfy the prerequisites for the courses you have selected?')
  	print('0) Yes')
  	print('1) No, want to know more about my selected courses')
  	self.input = int(input())
  	print('------------------------------------------------------------------------------------------------------------------------------------------------------------------')
  	if self.input == 0:
  		Student.preq_check(self, self.pre_req, self.lower_div, self.courses_selected)
  	else:
  		Student.input_know_more(self, len(self.courses_selected))
  #_______________________________________________________________________________________________________________________________________________________________
  def input_generator(self,choice):
  	if choice == 0:
  		print('------------------------------------------------------------------------------------------------------------------------------------------------------------------')
  		print('How many courses do you want to select?')
  		Student.input_loop(self,int(input()))
  	elif choice == 1:
  		print('------------------------------------------------------------------------------------------------------------------------------------------------------------------')
  		print('How many courses do you want to know more about?')
  		Student.input_know_more(self, int(input()))
  	elif choice == 2:
  		Student.input_know_more(self, len(self.searched))
  	elif choice == 3:
  		for c in self.searched:
  			self.courses_selected.append(c[0])
  		print('The courses you have selected are:', self.courses_selected)
  		print('Do you want to run a prerequisites check on them?')
  		e = str(input())
  		if e == 'Yes' or e == 'yes' or e == 'YES' or e == 'Y' :
  			Student.preq_check(self, self.pre_req, self.lower_div, self.courses_selected)
  		else:
  			print('Do you want to plan a schedule for your selected classes?')
  			one_input = str(input())
  			if one_input == 'Yes' or one_input == 'yes' or one_input == 'YES' or one_input == 'Y':
  				Student.plan_a_schedule(self, self.courses_selected)
  			else:
  				print('Thank you for using online EECS services')
  #_______________________________________________________________________________________________________________________________________________________________
  def interest_check(self, interest):
   	for key, value in dic2.items():
   	  	if interest in value:
   	  		self.found = key
   	self.searched = [[dic[c].code, dic[c].name] for c in dic.keys() if self.found in dic[c].keywords]
   	print('------------------------------------------------------------------------------------------------------------------------------------------------------------------')
   	print('The following courses match your interest')
   	print(self.searched)
   	print('------------------------------------------------------------------------------------------------------------------------------------------------------------------')
   	print('Would you want to select the searched courses or know more about specific courses or about all of them')
   	print('0) Select Courses')
   	print('1) Know more about specific courses')
   	print('2) Know more about all of them')
   	print('3) Select all those courses that I searched')
   	Student.input_generator(self,int(input()))
  #_______________________________________________________________________________________________________________________________________________________________
  def prereq_enter(self,inp):
  	if inp == 0:
  		print('Too early to start planning for upper division classes')
  	else:
  		for i in range(0, inp):
  			self.preq_taken = str(input())
  			self.pre_req.append(self.preq_taken)
  		print('----------------------------------------------------------------------------------------------------------------------------------')
  		print('Enter the lower-division requirements courses and any MATH courses you have taken after Math 1B you have taken. But, first How many have you taken?')
  		self.taken = int(input())
  		for i in range(0, self.taken):
  			self.lower_taken = str(input())
  			self.lower_div.append(self.lower_taken)
  		print('------------------------------------------------------------------------------------------------------------------------------------------------------------------')
  		print ('What fields of Computer Science are you interested in which are offered by Berkeley?')
  		Student.interest_check(self, str(input()))
  #_______________________________________________________________________________________________________________________________________________________________
  def major_check(self, inp):
  	if inp == 'Yes' or inp == 'YES' or inp == 'Y' or inp == 'yes':
  		self.pre_req = ['CS61A','CS61B','CS70']
  		print('------------------------------------------------------------------------------------------------------------------------------------------------------------------')
  		print('Enter the lower-division requirements courses and any MATH courses you have taken after Math 1B you have taken. But, first How many have you taken?')
  		self.taken = int(input())
  		for i in range(0, self.taken):
  			self.lower_taken = str(input())
  			self.lower_div.append(self.lower_taken)
  		print('------------------------------------------------------------------------------------------------------------------------------------------------------------------')
  		print ('What fields of Computer Science are you interested in which are offered by Berkeley?')
  		Student.interest_check(self, str(input()))
  	else:
  		print('------------------------------------------------------------------------------------------------------------------------------------------------------------------')
  		print('How many pre-requisites have you taken?')
  		self.prereq_enter(int(input()))
  #_______________________________________________________________________________________________________________________________________________________________
  def initial_check(self, first):
    if first == 0:
    	print('------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    	print('Are you a CS Major yet?')
    	Student.major_check(self, str(input()))
    else: 
    	print('Please seek an appointment with an EECS Advisor')

#____________________________________________________________________________CS MAJOR PRE_REQUISITES AND TOUGH COURSES_________________________________________________________________
pre_requisites = ['CS61A', 'CS61B', 'CS70']
tough_upperdivs = ['CS152', 'CS162', 'CS164','CS169','CS170', 'CS184', 'CS189']
#____________________________________________________________________________STUDENT SUBJECT SELECTION DICTIONARY ________________________________________________________
student_selections = {}
#__________________________________________________________________________________UPPPER DIVISION COURSES DICTIONARY ____________________________________________________________________________________
dic = {  'CS152': UpperDivision_Courses("CS152", "Computer Architecture and Engineering", ["hardware"],["CS61C"],"CS152 provides foundational knowledge for students seeking to learn about computer architecture. A handful of topics taught in this class may also help prepare students for operating systems courses, such as CS162. CS152 fulfills the design course requirement for EECS and L&S CS majors. This course is taught above the transistor/circuits abstraction, and focuses on the design of processors at a higher level. It begins with discussing important architectures in history, then moves on to ISA design, pipelining, memory hierarchy, and virtual memory. Several types of processors are then discussed, including out-of-order, superscalar, and vector processors." )
        ,'CS160': UpperDivision_Courses("CS160", "User Interface Design and Development",["gd","SE","tech"], ["CS61B"], "CS160 is an introduction to human-computer interaction and user interface design. The course teaches you how to prototype, evaluate, and design user interfaces. Students work in groups of 4-5 students in this project-based course. Unlike most other CS classes, CS160 does not focus in on specific algorithms, techniques, or technologies. Instead, it is about developing a broad set of skills relevant to user-focused design and implementation, which include ideation, assessment, communication, rapid prototyping, implementation, and evaluation. The course culminates in a large final group project that is proposed by your group and is an opportunity to apply the broad set of skills you acquire throughout the semester to a real project for real users. The implementation domain varies from semester to semester and from professor to professor. In recent history, Android is usually the chosen platform.")
        ,'CS161': UpperDivision_Courses("CS161", "Computer Security", ["Security","Core","Algorithms","internet","tech"],["CS61C", "MATH55" ,"CS70"],"This course is about security in a variety of domains, including the web, networking, operating systems, and cryptography. It goes over security techniques, programming involved to repel attacks, encryption, computer safety, networking basics, and other topics. It also frequently uses real-world stories and applications as case studies.")
        ,'CS162': UpperDivision_Courses("CS162", "Operating Systems and System Programming",["hardware","Algorithms","Core"], ["CS70","MATH55" ,"CS61C"],"The purpose of this course is to teach the design of operating systems and operating systems concepts that appear in other advanced systems. Topics covered include operating systems, systems programming, networked and distributed systems, and storage systems, including multiple-program systems (processes, interprocess communication, synchronization), memory allocation (segmentation, paging), resource allocation and scheduling, file systems, basic networking (sockets, layering, APIs, reliability), transactions, security and privacy.")
        ,'CS164': UpperDivision_Courses("CS164", "Programming Languages and Compilers",["Core","SE","Algorithms"], ["CS61B", "CS61C"],"CS164 is an introduction to the design of programming languages and the implementation of translators for them. In the class, you'll do some general exploration of programming language design and its implications for implementation, and look at a dialect of at least one particular language. One goal of the course is to explore the structure of programming languages and to consider alternatives to familiar programming language features. You'll also study the problem of translating programming languages into machine-executable forms, abstracted to a platform-agnostic language. You'll study language translation to learn some of techniques used that are useful for many programming problems outside of language translation, to gain a better intuitive feel for the tools used when programming and the costs of the programs, and to gain experience with the engineering problems associated with building and validating a substantial piece of software.")
        ,'CS169': UpperDivision_Courses("CS169", "Software Engineering",["SE","internet","DB","AI"], ["CS61A", "CS61B" ,"CS61C"],"CS169 is about all the things that go behind software engineering and software development.")
        ,'CS168': UpperDivision_Courses("CS168", "Introduction to the Internet: Architecture and Protocols", ["internet","hardware","Algorithms", "Security","tech"], ["CS61A", "CS61B", "MATH54", "MATH53"],"This course is an introduction to the Internet architecture. We will focus on the concepts and fundamental design principles that have contributed to the Internet's scalability and robustness and survey the various protocols and algorithms used within this architecture. Topics include layering, addressing, intradomain routing, interdomain routing, reliable delivery, congestion control, and the core protocols (e.g., TCP, UDP, IP, DNS, and HTTP) and network technologies (e.g., Ethernet, wireless).")
        ,'CS170': UpperDivision_Courses("CS170", "Efficient Algorithms and Intractable Problems", ["Algorithms","Core","ML","AI","Security","SE","tech"],["CS61B","CS70"],"CS 170 is an introductory course to theoretical computer science and surveys a variety of algorithm paradigms. Central concepts are algorithm design, algorithmic proofs, and running time analysis. The course also serves as an intro to complexity classes, exploring NP-completeness. The format of assignments is typically written problem sets, with psuedocode expected rather than compilable computer code.")
        ,'CS172': UpperDivision_Courses("CS172", "Computability and Complexity", ["Algorithms","Security","SE","AI"],["CS170"],"This course covers three main areas: automata theory, computability theory, and complexity theory. Automata theory explores what the basic mathematical models of computation are. Computability theory explores what problems can be solved by computers. Complexity theory explores what makes some problems computationally hard and others easy.")
        ,'CS176': UpperDivision_Courses("CS176", "Algorithms for Computational Biology", ["Algorithms"],["CS188", "CS70", "CS170", "EECS126"],"In 176, we study algorithms and data structures for many applications in Computational Biology. We discuss everything from genome searching, DNA alignment, evolutionary tree of life, and detecting coding regions. Note: There is no biology prereq for this course. The class focuses primarily on algorithms, only referencing biology as the motivation for certain problems.")
        ,'CS174': UpperDivision_Courses("CS174", "Combinatorics and Discrete Probability", ["Algorithms"], ["MATH55","CS70","EE126" ,"STAT134"],"Heavily involving Probability class.")
        ,'CS182': UpperDivision_Courses("CS182", "Designing, Visualizing and Understanding Deep Neural Networks", ["ML", "SE", "AI", "Security"],["MATH53" ,"MATH54", "CS70" ,"STAT134" ,"CS61B", "CS189"],' Deep Networks have revolutionized computer vision, language technology, robotics and control. They have growing impact in many other areas of science and engineering. They do not however, follow a closed or compact set of theoretical principles. In Yann Lecuns words they require "an interplay between intuitive insights, theoretical modeling, practical implementations, empirical studies, and scientific analyses." This course attempts to cover that ground.')
        ,'CS184': UpperDivision_Courses("CS184", "Computer Graphics",["gd","internet", "SE","AI"],["CS61B", "MATH54"],"Techniques of modeling objects for the purpose of computer rendering: boundary representations, constructive solids geometry, hierarchical scene descriptions. Mathematical techniques for curve and surface representation. Basic elements of a computer graphics rendering pipeline; architecture of modern graphics display devices. Geometrical transformations such as rotation, scaling, translation, and their matrix representations. Homogeneous coordinates, projective and perspective transformations. Algorithms for clipping, hidden surface removal, rasterization, and anti-aliasing. Scan-line based and ray-based rendering algorithms. Lighting models for reflection, refraction, transparency. Cameras and lenses. Color and perception. Animation, kinematics, physical simulation. Digital image processing and computational imaging; light field cameras.")
        ,'CS186': UpperDivision_Courses("CS186", "Databases", ["DB", "tech","ML"],["CS61B", "CS61C"],"Access methods and file systems to facilitate data access. Hierarchical, network, relational, and object-oriented data models. Query languages for models. Embedding query languages in programming languages. Database services including protection, integrity control, and alternative views of data. High-level interfaces including application generators, browsers, and report writers. Introduction to transaction processing. Database system implementation to be done as term project.")
        ,'CS188': UpperDivision_Courses("CS188", "Introduction to Artificial Intelligence",["SE","AI", "ML", "Security", "internet"],["CS61A","CS61B", "CS70" ,"MATH55"],"CS188 introduces the basic ideas and techniques underlying the design of intelligent computer systems with a specific emphasis on the statistical and decision-theoretic modeling paradigm. By the end of the course, you will have built autonomous agents that efficiently make decisions in stochastic and in adversarial settings, drawn inferences in uncertain environments, optimized actions for arbitrary reward structures, and created machine learning algorithms.")
        ,'CS189': UpperDivision_Courses("CS189", "Introduction to Machine Learning",["SE","AI", "ML", "Security", "internet","Algorithms"] ,["MATH53", "CS70", "CS188", "MATH54"],'The purpose of CS 189 is to provide an introduction to machine learning. Machine learning is chiefly concerned with understanding structures within data and applying these structures to solve problems that can involve predictions and clustering, among other statistical applications. In this course, the recurring example problems are making an email spam filter and a handwritten-digit recognizer. The course aims to provide theoretical foundations, algorithms, methodologies, and applications for machine learning, though it is more akin to a "bag of tools" class rather than one that focuses heavily on mathematical foundations (CS281A provides that). Topics may include supervised methods for regression and classification (linear models, decision trees, neural networks, ensemble methods, instance-based methods); generative and discriminative probabilistic models; Bayesian parametric learning; density estimation and clustering; Bayesian networks; time series models; dimensionality reduction; programming projects covering a variety of real-world applications.')
        ,'CS191': UpperDivision_Courses("CS191", "Quantum Information Science and Technology",["tech", "Algorithms"] ,["MATH54", "PHYSICS7B", "CS170"],"As an overview class, it provides a broad introduction to quantum computation theory, quantum algorithms, and physical implementations. As it is also cross-listed with Physics and Chemistry, the topics treated will not be extremely in-depth, since different sections of the class will appeal to different majors.")
    }
#_____________________________________________________________________KEYWORDS LISTS ____________________________________________________________________

dic2 = { 'tech': ['Upcoming Technology']
		 , 'AI': ['AI', 'Artificial Intelligence', 'Decision-making', 'Intelligence' 'Computer Intelligence','Cognitive Architecture']
		 , 'gd': ['Graphic Designing', 'Computer Graphics', 'Visual', 'Design', 'Bedroom Programming', 'Computer Generated Imagery', 'CGI', 'Computer Vision', 'Vision']
         , 'hardware': ['EE', 'Circuits', 'Electrical Engineering', 'Hardware', 'Operating Systems']
		 , 'ML': ['Blockchain','Machine Learning', 'ML', 'Predictions', 'Understanding Data Structures', 'Clustering Data', 'Application of Data']
		 , 'DB': ['Data Architecture','Databases', 'Database', 'DBMS', 'Database Management System', 'Table Relationships','Studying Data', 'Analysing Data', 'Big Data', 'Data']
		 , 'SE': ['Testing', 'Software', 'Software Engineering', 'User interface design', 'User interface','SDLC', 'Systems Development Life Cycle', 'Systems Development' ]
		 , 'Security': ['Security', 'Cyber Security', 'Protection from Viruses', 'Ransomware', 'Viruses', 'Cryptography']
		 , 'Core': ['Functional Programming','Distributed Computing','Interpreters', 'Compilers', 'Programming Languages', 'Development of Programming Languages']
		 , 'Algorithms': ['Command Interpreter','Brute Force Programming', 'Natural Language Processing', 'Algorithms', 'Run-time', 'Computational Biology', 'Mathematics & CS', 'Maths & CS', 'Math & CS', 'Mathematics & Computer Science', 'Physics & CS']
         , 'internet': ['Routing','Content Management System','CMS','Internet', 'Web', 'WWW', 'World Wide Web', 'Web Development', 'Cloud Computing']
        }
#________________________________________________________________*********BEGINNER TESTS************_____________________________________________________
print("Welcome to SuitableFind")
print("Can you please enter your name?")
name = str(input())
name = Student(name)
print('How can we help you?')
print('0) Help with CS Upperdivision courses selection?')
print('1) Understanding the EECS Major')
inp = int(input())
name.initial_check(inp)
