# Neurosymbolic Reasoning Shortcuts

Educational materials for exploring reasoning shortcuts and concept
grounding in neurosymbolic learning.

## Interactive lesson

**Right Answer, Wrong Concept**

If a model gets the right answer, how do we know it learned the
concepts we intended?

A *reasoning shortcut* is a learned concept distribution that attains maximal
or near maximal likelihood on the training objective while diverging from
ground truth concept semantics. Both conditions are required: a low concept
score on its own is equally consistent with an undertrained model, which is an
ordinary engineering failure with an ordinary fix. Telling those apart is what
these materials teach.

## Learning goals

Learners will:

- explain reasoning shortcuts in neurosymbolic learning
- distinguish task performance from concept quality
- evaluate learned concept grounding
- investigate why additional data may not eliminate reasoning shortcuts
- experiment with mitigation strategies such as concept supervision
  and multi-task learning
- examine implications for out-of-distribution generalization

## Materials

### Interactive lesson

`slides/index.html` is a 31 slide reveal.js deck in eight sections: Puzzle,
Structure, Inspect, Constrain, Transfer, Measure, Position, Challenge. It
opens on Clever Hans as a cross-domain hook and closes on a learner challenge.

Open it directly in a browser. No build step and no network access are
required, because reveal.js is vendored in `reveal.js/dist/`.

```
# macOS / Linux
open slides/index.html

# Windows
start slides/index.html
```

Press `S` for speaker notes and `Esc` for the slide overview.

### Notebook

`reasoning_shortcuts.ipynb` is a hands-on notebook for creating, detecting and
mitigating reasoning shortcuts. Every diagnostic in the deck is runnable here
end to end.

```
pip install -r requirements.txt
jupyter notebook reasoning_shortcuts.ipynb
```

MNIST downloads automatically on first run via `torchvision.datasets`, so the
`data/` directory is not tracked in this repository.

### Case study

An autonomous driving example connecting the phenomenon to real world
perception, presented as an application and transfer exercise rather than a
fourth controlled demonstration.

## What the materials cover

The lesson is organised around the four factors that Marconato et al. (2023)
identify as governing whether a reasoning shortcut exists, each with the
mechanism that produces it and the diagnostic that exposes it.

| Factor | Worked example | Diagnostic |
| --- | --- | --- |
| Prior knowledge `K` | 3-way XOR, exhaustive | enumerate the label optimal mappings of the rule |
| Concept extractor architecture | MNIST-Addition | swap encoder with data and rule held fixed, check the ceiling, read the confusion matrix |
| Learning objective | Add and Multiply | add a second relationship over the same concepts |
| Data structure and support | driving scenario | per concept F1 plus a decorrelated shift test |

In every case task accuracy stays at or near its ceiling while concept quality
varies from 0.998 down to 0.000. Task accuracy flags none of them.

## Key references

- Marconato, Teso, Vergari & Passerini (2023). *Not All Neuro-Symbolic Concepts Are Created Equal: Analysis and Mitigation of Reasoning Shortcuts.* NeurIPS. [arXiv:2305.19951](https://arxiv.org/abs/2305.19951)
- Bortolotti, Marconato, Carraro, Morettin et al. (2024). *A Neuro-Symbolic Benchmark Suite for Concept Quality and Reasoning Shortcuts.* NeurIPS Datasets & Benchmarks. [arXiv:2406.10368](https://arxiv.org/abs/2406.10368)
- Marconato, Bortolotti, van Krieken, Vergari, Passerini & Teso (2024). *BEARS Make Neuro-Symbolic Models Aware of their Reasoning Shortcuts.* UAI. [arXiv:2402.12240](https://arxiv.org/abs/2402.12240)
- Yang et al. (2024). *Analysis for Abductive Learning and Neural-Symbolic Reasoning Shortcuts.* ICML.
- van Krieken, Minervini, Ponti & Vergari (2025). *Neurosymbolic Reasoning Shortcuts under the Independence Assumption.* NeSy. [arXiv:2507.11357](https://arxiv.org/abs/2507.11357)
- Takemura, Inoue & Nishino (2026). *Constraint-Based Analysis of Reasoning Shortcuts in Neurosymbolic Learning.* [arXiv:2604.23377](https://arxiv.org/abs/2604.23377)
- Coston (2026). *Falsifying Discriminant Validity of Predictive Algorithms.* [arXiv:2601.17146](https://arxiv.org/abs/2601.17146)

## Third party materials

Two figures in the deck are reproduced from rsbench (Bortolotti, Marconato et
al., 2024, [arXiv:2406.10368](https://arxiv.org/abs/2406.10368)), which is
published under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). They are
reproduced verbatim with attribution in the slide captions:

- `slides/assets/rsbench_fig2_bdd_infer_train.png` (Fig. 2, a NeSy predictor on a BDD-OIA dashcam frame)
- `slides/assets/rsbench_dpl_confusion.png` (Table 3 left, DeepProbLog concept confusion on MNAdd-EvenOdd)

All other figures and diagrams are original to this repository.
`slides/assets/entangled_confusion.png` is generated by the notebook.

`reveal.js/` vendors [reveal.js](https://github.com/hakimel/reveal.js) v6 under
the MIT licence; see `reveal.js/LICENSE`.

## Licence

MIT, see `LICENSE`. The reproduced rsbench figures remain under CC BY-SA 4.0
as noted above.
