// Data for your project; you'd typically fetch this from a database or API
const projects = [
  {
    title: "Project 1",
    description: "This is a machine learning project that does XYZ.",
    technologies: ["Python", "TensorFlow"],
    link: "https://github.com/yourusername/project1"
  }
  {
    title: "Linear Regression for Sales Prediction",
    description: "A Machine Learning model to predict next month's sales based on 11 historical data points.",
    technologies: ["Python", "scikit-learn"],
    link: "https://github.com/yourusername/linear-regression-sales-prediction"
  }
  // Add more projects here
];

// Function to create project card
function createProjectCard(project) {
  const projectCard = document.createElement("div");
  projectCard.className = "project-card";

  const title = document.createElement("h2");
  title.innerText = project.title;
  projectCard.appendChild(title);

  const description = document.createElement("p");
  description.innerText = project.description;
  projectCard.appendChild(description);

  const technologies = document.createElement("p");
  technologies.innerText = "Technologies used: " + project.technologies.join(", ");
  projectCard.appendChild(technologies);

  const link = document.createElement("a");
  link.innerText = "Github Repo";
  link.href = project.link;
  projectCard.appendChild(link);

  return projectCard;
}

// Append projects to the container
const projectContainer = document.getElementById("project-container");

projects.forEach(project => {
  const projectCard = createProjectCard(project);
  projectContainer.appendChild(projectCard);
});
