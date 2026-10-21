export interface Project {
  id: string;
  title: string;
  role: string;
  client: string;
  period: string;
  tagline: string;
  description: string;
  highlights: string[];
  stack: string[];
  image: string;
  link?: string;
  badge: string;
  badgeColor: 'magenta' | 'cyan' | 'green' | 'yellow' | 'purple';
}

export interface WebProject {
  id: string;
  domain: string;
  url: string;
  title: string;
  category: string;
  description: string;
  stack: string[];
  features: string[];
  status: string;
  badgeColor: 'magenta' | 'cyan' | 'green' | 'yellow' | 'purple';
}

export interface CareerEntry {
  title: string;
  company: string;
  type: string;
  period: string;
  location?: string;
  description: string;
  details: string[];
  tech: string[];
  status: 'CURRENT' | 'PREVIOUS';
}

export const PERSONAL_INFO = {
  name: "Martin Kolda",
  title: "Python AI & Full-Stack Web Developer",
  status: "Available for AI Engineering & Modern Web Projects",
  location: "Czech Republic",
  email: "mkko@seznam.cz",
  github: "https://github.com",
  summary: "AI Developer specialized in enterprise-grade Python solutions, RAG pipelines, and conversational agents, paired with ultra-fast modern web development in Astro and Next.js.",
  currentFocus: "Architecting high-impact AI systems for ČEZ a.s. & crafting hyper-performant client web experiences.",
};

export const AI_PROJECTS: Project[] = [
  {
    id: "cez-ai",
    title: "Enterprise AI Solutions",
    role: "Lead AI Developer (Živnostník)",
    client: "ČEZ a.s.",
    period: "02/2025 – Present",
    tagline: "Architecting mission-critical generative AI and predictive systems for Central Europe's largest energy utility.",
    description: "Developing specialized AI architectures for ČEZ a.s., integrating modern LLMs, autonomous agent workflows, and data pipelines to optimize industrial operations, knowledge retrieval, and enterprise efficiency.",
    highlights: [
      "Designed secure enterprise LLM inference pipelines with strict data privacy guarantees",
      "Built specialized agentic workflows for operational domain reasoning",
      "Engineered automated knowledge retrieval indexing across heterogenous documentation",
      "Delivered robust Python backends with automated validation and monitoring"
    ],
    stack: ["Python 3.12+", "Enterprise LLMs", "LangChain", "FastAPI", "VectorDB", "PostgreSQL", "Docker", "REST API"],
    image: "/images/cez-ai-8bit.svg",
    badge: "ACTIVE ENTERPRISE",
    badgeColor: "green"
  },
  {
    id: "robosales",
    title: "AI Shopping Assistant",
    role: "Contract AI Developer",
    client: "robosales.ai",
    period: "Contractor Project",
    tagline: "Next-gen conversational commerce assistant that drives user conversion and product discovery.",
    description: "Engineered an intelligent conversational AI shopping assistant that guides buyers through multi-attribute product catalogs, answers queries in natural language, and seamlessly collects buyer requirements.",
    highlights: [
      "Created dynamic interactive shopping form powered by LLM intent extraction",
      "Designed conversational product recommendation logic with context retention",
      "Integrated lead qualification and automated notification workflows",
      "Achieved sub-second response times for smooth user interactions"
    ],
    stack: ["Python", "FastAPI", "LLM APIs", "JSON Schema", "Prompt Engineering", "Webhooks", "E-commerce Engine"],
    image: "/images/robosales-8bit.svg",
    badge: "E-COMMERCE AI",
    badgeColor: "magenta"
  },
  {
    id: "addai",
    title: "LangChain RAG & Data Management Platform",
    role: "AI / Python Developer",
    client: "AddAI.Life",
    period: "03/2024 – 02/2025 (1 yr)",
    tagline: "High-throughput retrieval-augmented generation search engines and S3/Postgres data management.",
    description: "Built core RAG search components and data ingestion infrastructure, enabling companies to turn massive unstructured document repositories into verified generative knowledge bases.",
    highlights: [
      "Engineered core RAG search component using LangChain and custom vector rerankers",
      "Built end-to-end CRUD data management application for multi-tenant RAG datasets",
      "Architected data storage across AWS S3, PostgreSQL, and scalable VectorDBs",
      "Implemented chunking, embedding generation, and metadata filtering strategies"
    ],
    stack: ["Python", "LangChain", "AWS S3", "PostgreSQL", "VectorDB", "FastAPI", "Docker", "PyTest"],
    image: "/images/websites-8bit.svg",
    badge: "CORE RAG PLATFORM",
    badgeColor: "purple"
  }
];

export const WEB_PROJECTS: WebProject[] = [
  {
    id: "b2ts",
    domain: "b2ts.cz",
    url: "https://b2ts.cz",
    title: "B2TS – Business & Tech Solutions",
    category: "Corporate & Technology Consulting",
    description: "Modern, high-performance company presentation website with optimized typography, responsive layouts, and lightning-fast loading speeds.",
    stack: ["Astro / Next.js", "TypeScript", "Tailwind CSS", "Netlify Forms"],
    features: [
      "Zero-latency static generation with instant navigation",
      "Serverless contact form with spam protection & Netlify integration",
      "100/100 Core Web Vitals score across mobile and desktop",
      "Clean corporate identity and structured content presentation"
    ],
    status: "LIVE PRODUCTION",
    badgeColor: "cyan"
  },
  {
    id: "vpt-lipno",
    domain: "vpt-lipno.cz",
    url: "https://vpt-lipno.cz",
    title: "VPT Lipno – Lake Resort & Accommodation",
    category: "Hospitality & Tourism Portal",
    description: "Engaging vacation rental portal for accommodation at Lake Lipno. Built to drive bookings with rich galleries, local activity guides, and direct inquiry forms.",
    stack: ["Astro", "TypeScript", "Responsive CSS", "Image Optimization"],
    features: [
      "High-res lazy loaded visual photo tours of apartments and lakeside surroundings",
      "Interactive booking reservation inquiry workflow",
      "SEO-optimized local tourism guides (skiing, sailing, hiking)",
      "Mobile-first responsive UX tailored for travelers on the go"
    ],
    status: "LIVE PRODUCTION",
    badgeColor: "yellow"
  },
  {
    id: "doteku",
    domain: "doteku.cz",
    url: "https://doteku.cz",
    title: "Doteku – Touch & Wellness Sanctuary",
    category: "Wellness & Body Therapy Studio",
    description: "Atmospheric, soothing web presence for a premier massage and wellness studio, featuring clear service menus, pricing, and client inquiry channels.",
    stack: ["Modern Web Stack", "TypeScript", "Custom CSS", "Netlify Forms"],
    features: [
      "Serene, elegant design aesthetic evoking tranquility and luxury",
      "Clear service catalogue with pricing, duration, and practitioner details",
      "Seamless mobile appointment inquiry and client data capture",
      "Fast page loads ensuring minimal drop-off rate"
    ],
    status: "LIVE PRODUCTION",
    badgeColor: "magenta"
  }
];

export const CAREER_HISTORY: CareerEntry[] = [
  {
    title: "AI Developer",
    company: "Živnostník (Freelance / Independent)",
    type: "Contract / Independent",
    period: "02/2025 – Present",
    location: "Czech Republic",
    description: "Delivering high-end Artificial Intelligence solutions for ČEZ a.s. and independent enterprise clients.",
    details: [
      "AI solution design & deployment for ČEZ a.s.",
      "Custom generative AI assistants and RAG orchestration",
      "Python enterprise system integration and secure API endpoints"
    ],
    tech: ["Python", "Enterprise LLMs", "LangChain", "FastAPI", "VectorDB", "PostgreSQL"],
    status: "CURRENT"
  },
  {
    title: "Web Developer (Vývojář webových stránek)",
    company: "Na volné noze (Freelance)",
    type: "Freelance",
    period: "12/2024 – Present",
    location: "Czech Republic",
    description: "Crafting bespoke, ultra-fast websites and web applications for businesses and regional brands.",
    details: [
      "Building with Next.js & Astro frameworks combined with TypeScript",
      "Automated lead capture using Netlify Forms and webhook integrations",
      "Shipped client portals including b2ts.cz, vpt-lipno.cz, and doteku.cz",
      "Obsessive focus on Core Web Vitals, accessibility, and clean responsive design"
    ],
    tech: ["Astro", "Next.js", "TypeScript", "Netlify", "Tailwind CSS", "Modern Web Standards"],
    status: "CURRENT"
  },
  {
    title: "AI / Python Developer",
    company: "AddAI.Life",
    type: "Full-Time (Na plný úvazek)",
    period: "03/2024 – 02/2025 (1 yr)",
    location: "Řevnice, Czech Republic",
    description: "Engineered core RAG search components and data management infrastructure for enterprise knowledge retrieval.",
    details: [
      "RAG search component implementation in Langchain",
      "CRUD data management application for multi-modal RAG systems",
      "Data layer integration with AWS S3, PostgreSQL, and specialized VectorDBs",
      "Prompt orchestration and retrieval ranking evaluations"
    ],
    tech: ["Python", "LangChain", "AWS S3", "PostgreSQL", "VectorDB", "FastAPI", "Docker"],
    status: "PREVIOUS"
  }
];

export const SKILLS_MATRIX = [
  { category: "AI & LLM Orchestration", skills: ["LangChain", "LlamaIndex", "RAG Systems", "Vector Databases", "Prompt Engineering", "Agentic Workflows"], level: 95 },
  { category: "Python Ecosystem", skills: ["Python 3.12+", "FastAPI", "AsyncIO", "PyTest", "Celery", "SQLAlchemy"], level: 98 },
  { category: "Storage & Data Ops", skills: ["PostgreSQL", "pgvector", "AWS S3", "Chroma / Qdrant", "Redis", "Docker"], level: 90 },
  { category: "Modern Frontend", skills: ["Astro", "TypeScript", "Next.js", "Modern CSS / TUI", "Netlify Forms", "Core Web Vitals"], level: 92 },
];
