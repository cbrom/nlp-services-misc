import SemanticRoleLabeling from './components/demos/SemanticRoleLabeling';

// This is the order in which they will appear in the menu
const modelGroups = [
    {
        label: "Annotate a sentence",
        models: [
            {model: "semantic-role-labeling", name: "Semantic Role Labeling", component: SemanticRoleLabeling}
        ]
    }
]

// Create mapping model => component
let modelComponents = {}
modelGroups.forEach((mg) => mg.models.forEach(({model, component}) => modelComponents[model] = component));

export { modelComponents, modelGroups }
