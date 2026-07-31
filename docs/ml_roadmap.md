# From Microbiology to ML Engineer: 5-Month Pre-Bioinformatics Roadmap
*July 30, 2026 → January 2027 (BSc Hons start)*

**Assumptions:** ~5 hrs/day, 5–6 days/week alongside a job = ~130–150 hrs/month, ~650–750 hrs total. That is genuinely a lot of runway — comparable to a full semester of focused coursework. Treat burnout risk seriously: build in 1 rest day/week, non-negotiable.

**Goal for January:** Not "expert." The goal is: solid math foundations, real Python/data fluency, understanding of classical ML + basic deep learning from first principles, and 2–3 small but real projects (ideally with a biology angle) you can talk about intelligently. That's what lets you hit the ground running in your BSc Hons and identify a thesis direction early.

---

## Month 1 (Aug): Math Foundations + Python for Data

**Math (1.5–2 hrs/day):**
- Linear algebra: 3Blue1Brown "Essence of Linear Algebra" (YouTube, ~3 hrs total) for intuition, THEN MIT OCW 18.06 (Gilbert Strang) lectures + problem sets for rigor. Don't skip the intuition step — it's what makes the rigor stick.
- Probability & statistics: Khan Academy Statistics/Probability track, start now, will bleed into Month 2.

**Python (1.5–2 hrs/day):**
- If Python basics are shaky at all: freeCodeCamp Python course or CS50P (CS50's Intro to Programming with Python) — has autograded problem sets with hints, exactly the format you like.
- Then: numpy, pandas, matplotlib — Kaggle Learn's "Python," "Pandas," "Data Visualization" micro-courses (all free, exercise-based).

**Output by end of Month 1:** Comfortable manipulating arrays/dataframes, plotting data, and you can explain matrix multiplication, dot products, and eigenvectors without notes.

---

## Month 2 (Sep): Probability/Stats + Classical ML Theory

**Math (1–1.5 hrs/day):**
- Finish Khan Academy probability/stats.
- Calculus refresher only as needed: Khan Academy Multivariable Calculus (focus on gradients/partial derivatives — that's the part ML actually uses).
- Start "Mathematics for Machine Learning" (free book by Deisenroth, Faisal, Ong — pdf is free online) as a reference, don't read cover to cover.

**ML (2.5–3 hrs/day):**
- Andrew Ng's Machine Learning Specialization (Coursera — audit for free, you lose the certificate and graded assignments but can still watch everything and code along using the public GitHub notebooks/exercises that mirror the course).
- StatQuest with Josh Starmer (YouTube) alongside — best plain-English explanations of regression, decision trees, random forests, gradient boosting, PCA, etc. Watch these *before* the lecture on the same topic if the Ng lecture is dense.

**Output by end of Month 2:** You understand and can implement from scratch (numpy only, no sklearn) linear regression, logistic regression, and gradient descent. You understand bias/variance, train/test/val splits, overfitting.

---

## Month 3 (Oct): Classical ML in Practice + First Project

**ML practice (2.5 hrs/day):**
- Kaggle Learn: Intro to ML, Intermediate ML, Feature Engineering micro-courses.
- Start using scikit-learn properly: pick a Kaggle "Getting Started" competition (Titanic, or better — look for a genomics/health dataset on Kaggle) and build a full pipeline: EDA → cleaning → feature engineering → model → evaluation.

**Math/theory reinforcement (1–1.5 hrs/day):**
- Fill gaps as they come up. By now you should be reading ML papers/blog posts and understanding most of the notation without panic — if not, that's your signal to go back to 3Blue1Brown/Khan Academy on the specific gap.

**Output by end of Month 3:** Project #1 done — a classical ML project, ideally with a biological dataset (gene expression, protein data, epidemiological data — Kaggle and UCI ML Repository both have these). Put it on GitHub with a clean README.

---

## Month 4 (Nov): Deep Learning Foundations

**Deep learning (3–3.5 hrs/day):**
- fast.ai "Practical Deep Learning for Coders" Part 1 — top-down, you're training real models in lesson 1.
- In parallel or right after: Andrej Karpathy's "Neural Networks: Zero to Hero" (YouTube) — you build backprop and a tiny neural net from raw Python/numpy, then work up to a GPT. This is the best free resource on Earth for *actually understanding* what's happening under the hood, not just calling `.fit()`. Use Claude/an LLM as your tutor here exactly as you planned — ask it to explain any line you don't follow, quiz you, or generate extra practice problems in the same style.

**Math as-needed (0.5–1 hr/day):**
- Chain rule / backprop math, softmax, cross-entropy loss — pull from Mathematics for ML book or 3Blue1Brown's neural network series as needed.

**Output by end of Month 4:** You've trained a neural net from scratch (no framework) and also a PyTorch model on real data (image or tabular). You understand backprop well enough to explain it on a whiteboard.

---

## Month 5 (Dec): Second Project + Bioinformatics Bridge

**Project (3–4 hrs/day):**
- Build Project #2: something that explicitly bridges biology and ML — e.g., a sequence classification model (DNA/protein), a simple drug-response prediction model, or an analysis of a public genomics dataset with an ML model on top. This is the project that will make your BSc Hons thesis conversations easy and will differentiate you from generic ML portfolios.
- Look at what tools your BSc Hons bioinformatics program uses (check the syllabus if available) and make sure you're not blindsided — e.g., R, Bioconductor, specific genomics file formats (FASTA/FASTQ/BAM).

**Wrap-up (1 hr/day):**
- Clean up both projects, write clear READMEs, put them on GitHub, maybe a short write-up on a free blog (even a GitHub Pages site) explaining what you built and why. This becomes your portfolio from day one of your degree.

**Output by end of Month 5 / January:** Two solid projects, strong math + classical ML + deep learning fundamentals, and a specific idea of what kind of thesis work interests you (e.g., "I want to work on ML for genomic sequence analysis" vs. general statements).

---

## Ongoing/parallel habits (all 5 months)
- **1 LeetCode-style problem 3x/week** (easy/medium, Python) — not because you're going into pure SWE, but coding fluency compounds and helps in every project. NeetCode.io has free structured lists.
- **Read 1 ML/bio-ML blog post or paper abstract per week** — even if you don't fully understand it yet. Builds vocabulary and pattern recognition over time.
- **Keep a simple log** of what you learned each week — helps you see progress and gives you material for a CV/personal statement later.

## During your BSc Hons and beyond (brief signposts)
- Look for a supervisor doing computational/quantitative work early — thesis choice matters more than most people realize.
- Apply for any remote ML/bioinformatics internships or research assistantships during your degree, even unpaid short ones — real project experience with a real team is worth more than another course.
- Decide Track A (industry ML engineer after MSc) vs Track B (PhD in computational biology/ML) based on how much you enjoy independent research vs. building things — you don't have to decide now.
- Keep building a public portfolio (GitHub, maybe Kaggle competitions) the whole way through — this is what actually gets you hired, PhD or not.

## Reality check to hold onto
This plan gets you to "genuinely competent, hireable junior ML person with a real biology edge" by the time you finish your BSc Hons — that's an excellent outcome and not a fantasy at all. "Working at Anthropic" is possible but is a long-shot stretch goal for nearly everyone in the world, not a realistic near-term milestone — don't let it be the measure of whether this path is working. Measure yourself against: are my projects getting better, do I understand more each month, am I becoming someone a hiring manager would trust with real problems.
