---
name: Jade Aerospace
description: A website laid out like a delivered satellite scene product. Imagery fills the page and the facts sit in thin metadata strips.
colors:
  ground: "#061418"
  ground-2: "#0A1E23"
  ink: "#F2F5F4"
  ink-2: "#B9CBC9"
  ink-3: "#7F9A98"
  rule: "#1E3A40"
  rule-2: "#2C5158"
  jade: "#51BAC1"
  peach: "#F6CDB4"
typography:
  display:
    fontFamily: "Space Grotesk, Noto Sans SC, system-ui, sans-serif"
    fontSize: "clamp(46px, 8.2vw, 104px)"
    fontWeight: 500
    lineHeight: 0.95
    letterSpacing: "-0.04em"
  headline:
    fontFamily: "Space Grotesk, Noto Sans SC, system-ui, sans-serif"
    fontSize: "clamp(34px, 4.6vw, 64px)"
    fontWeight: 500
    lineHeight: 1.02
    letterSpacing: "-0.025em"
  title:
    fontFamily: "Space Grotesk, Noto Sans SC, system-ui, sans-serif"
    fontSize: "clamp(19px, 1.6vw, 22px)"
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: "-0.01em"
  body:
    fontFamily: "Manrope, Noto Sans SC, system-ui, sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "Space Grotesk, Noto Sans SC, system-ui, sans-serif"
    fontSize: "12px"
    fontWeight: 500
    letterSpacing: "0.07em"
  figure:
    fontFamily: "Geist Mono, ui-monospace, Menlo, monospace"
    fontSize: "clamp(26px, 2.6vw, 38px)"
    fontWeight: 500
    lineHeight: 1
    letterSpacing: "-0.03em"
    fontFeature: "\"tnum\""
rounded:
  none: "0px"
spacing:
  gutter: "clamp(16px, 3.2vw, 40px)"
  grid-gap: "24px"
  section: "clamp(88px, 11vw, 160px)"
  container: "1360px"
  top-bar: "60px"
components:
  button-primary:
    backgroundColor: "{colors.jade}"
    textColor: "{colors.ground}"
    rounded: "{rounded.none}"
    padding: "14px 22px"
  button-primary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ground}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "14px 22px"
  nav-contact:
    backgroundColor: "{colors.jade}"
    textColor: "{colors.ground}"
    rounded: "{rounded.none}"
    padding: "8px 16px"
  tag-status:
    backgroundColor: "transparent"
    textColor: "{colors.jade}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "3px 7px"
  tag-planned:
    backgroundColor: "transparent"
    textColor: "{colors.peach}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "3px 7px"
  collar-cell:
    textColor: "{colors.ink}"
    typography: "{typography.figure}"
    padding: "16px 24px 18px"
  input-line:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: "8px 0 10px"
---

# Design System: Jade Aerospace

## Overview

**Creative North Star: "The Scene Product"**

Every page reads like a delivered satellite image product rather than a startup landing page. Photographs and scenes take most of the surface. Each one sits in a thin frame with jade corner marks, like the registration ticks on an image tile. Facts live in hairline metadata strips: a four-cell "collar" under the hero scene, ruled spec tables, and a dated ledger. Corners are square and lines are 1px. The background is a near-black viewing ground, the kind of dark field an image analyst looks at scenes on.

The page reads from top to bottom as a chain from orbit to the field. A fixed stage rail on the left side of wide screens tracks your position like an altitude readout. Scale-bar dividers mark the move from one stage of the chain to the next. Motion is slow and settling: the hero image eases into place, and each frame's corner ticks draw in as it scrolls into view.

Colour is held back. White and two grey-jade inks carry the text, jade marks rules and active states, and peach appears only where something has not happened yet.

**Key Characteristics:**
- Near-black ground, white type, jade hairlines and active states
- Square corners everywhere (0px radius), 1px rules, no shadows
- Images always sit in a frame with corner ticks, with a metadata caption below
- Measured values are set in Geist Mono with tabular figures; all other text uses Space Grotesk (display) or Manrope (body)
- Peach means "planned / target / not done", nothing else
- English and Chinese pages are built as matching pairs

## Colors

A dark, cool palette: one jade accent on a near-black blue-green ground, plus one warm signal colour kept for the future tense.

### Primary
- **Survey Jade** (jade): hairlines that need to be noticed, the corner ticks on every frame, the active stage on the rail, small caps labels for categories (frequency bands, roles, channels), year figures in the ledger, the primary button fill, focus outlines, text selection, and the caret.

### Secondary
- **Planned Peach** (peach): marks only planned, target or not-yet-done states, such as the "first launch target" collar figure, "Target" tags, planned ledger rows (year and status), and the contact form's failed-send message. It never decorates.

### Neutral
- **Viewer Ground** (ground): the page background, the top bar, and image scrims (as rgba of the same hue, at 0.55 to 0.92).
- **Raised Ground** (ground-2): the contact band, the hover state on ledger rows, and the plates behind the globe image and the calibration schematic.
- **Scene White** (ink): headlines, primary text, and collar figures.
- **Jade Grey** (ink-2): paragraphs under headlines, table support text, and captions in bold.
- **Label Grey** (ink-3): small-caps labels, spec-table row headings, notes, and the footer. It keeps at least 4.5:1 contrast on the ground.
- **Hairline** (rule): the default 1px rule for tables, ledgers, section dividers, and the borders on secondary frames.
- **Strong Hairline** (rule-2): borders on the hero frame and full-bleed frames, collar dividers, input underlines, the email copy row, and the scrollbar thumb.

### Named Rules
**The Future Tense Rule.** Peach marks only things that have not happened yet (planned, target) or have just failed. If something is done, filed or granted, it is jade or white. Never use peach as decoration or as a second accent.

**The Hairline Rule.** Structure comes from 1px lines in rule or rule-2, never from filled card backgrounds. Use jade for a line only when it marks a state: the current row, the active stage, or a focus.

## Typography

**Display Font:** Space Grotesk (falls back to Noto Sans SC, then system-ui)
**Body Font:** Manrope (falls back to Noto Sans SC, then system-ui)
**Label/Mono Font:** Geist Mono (falls back to ui-monospace, then Menlo), used for measured values only

**Character:** Space Grotesk brings an engineered, slightly technical edge to headlines and labels. Manrope keeps long reading calm. Geist Mono with tabular figures makes numbers read like instrument output.

### Hierarchy
- **Display** (500, clamp 46 to 104px, line-height 0.95, tracking -0.04em): the hero headline only, set low-left on the scene.
- **Headline** (500, clamp 34 to 64px, line-height 1.02, tracking -0.025em): section headings. Inside the overlay on full-bleed images it steps down to clamp 30 to 52px.
- **Title** (500, clamp 19 to 22px, line-height 1.2): names and small headings. Pilot scene sheets use a larger step (clamp 24 to 32px).
- **Body** (Manrope 400, 17px, line-height 1.6; 16px under 760px): paragraphs. Section intros are clamp 17 to 19px, held to 62ch, in ink-2. Supporting copy in tables, ledgers and lists is 15 to 15.5px.
- **Label** (Space Grotesk 500, 12px, tracking 0.07em, uppercase): captions, spec-table row headings, tags, the rail, ledger status, roles, and the hero scene ID. This is the metadata voice of the scene.
- **Figure** (Geist Mono 500, tabular figures): collar values (clamp 26 to 38px), ledger years (18px), inline numbers in spec tables (16px), and the email address.

### Named Rules
**The Measured Value Rule.** Monospace is for numbers that were measured, counted or dated (satellites, planes, sites, metres, years) and for the email address. Don't set prose, headings or labels in mono.

**The CJK Leading Rule.** On Chinese pages, headings use 0 tracking and a looser line-height (1.18, and 1.08 for the hero). Never apply the negative Latin tracking to Chinese text.

## Layout

The container is up to 1360px wide, with a fluid side gutter (clamp 16 to 40px). Content sits on a 12-column grid with 24px gaps. Section heads take columns 1 to 8 (the intro text, 1 to 7), so the right side stays open. Sections open with clamp 88 to 160px of top padding and have a 60px scroll offset for the fixed top bar (56px under 760px).

Recurring compositions:
- **Hero scene:** one full-viewport image inside an inset frame (gutter on all sides). The headline sits low-left, and a four-cell collar is pinned to the bottom edge.
- **Media and spec:** an image across columns 1 to 7, a spec table across 8 to 12, aligned to the bottom.
- **Full bleed:** an image the full width of the gutter at 21:9 (minimum 420px), with a text overlay docked bottom-left, then a caption, then a row of ruled cells.
- **Scene sheets:** alternating image and text rows (image across 7 columns, text across 5), swapping sides on even rows.
- **Contact sheet:** a 4-up grid of square scenes on 2px rule-coloured gutters.
- **Ledger:** full-width ruled rows with year, title, detail and status columns.

Breakpoints are 1280px (the stage rail appears and main content gets 110px of left padding), 1100px (multi-column splits collapse to one column; the team and ruled cells go 2-up; the nav keeps only the language switch and Contact), and 760px (the hero image stacks above the copy; the collar, contact sheet and photo strips go 2-up; pilots and cases go 1-up).

**The Scale Bar Rule.** Use a scale bar (four alternating filled and empty 48px segments) to divide one stage of the chain from the next. It sits at the start of a stage section and is decorative only (aria-hidden). Don't use it as a general section ornament.

## Elevation & Depth

The system is flat. No box-shadows are used anywhere. Depth comes from three things: images sitting under dark gradient scrims of the ground colour so text stays legible, translucent ground panels laid over images (the collar at 0.78 opacity, the full-bleed overlay at 0.9), and the single raised tone (ground-2) for the contact band and image plates.

**The No-Shadow Rule.** Separate layers with a hairline or a tonal step, never a drop shadow, glow or blur.

## Shapes

Every corner is square (0px): buttons, tags, inputs, frames, plates and tables. The repeated geometric signature is the corner tick: four jade L-marks (22px arms, 2px thick) drawn at the corners of every image frame. Borders are always 1px. Inputs are a single bottom rule, not a box. The stage rail uses 7px square markers, not dots. The only round shape on the site is the globe image (see Components).

## Components

### Buttons
Flat, square, with a technical feel.
- **Shape:** square corners (0px), 1px border, Space Grotesk 500 at 15px, with an optional 14px inline SVG arrow.
- **Primary:** jade fill, ground text, 14px 22px padding.
- **Hover / Focus:** the fill and border switch to ink (white) over 0.2s. Focus shows a 2px jade outline offset by 3px.
- **Ghost:** transparent, ink text, border of ink at 50% opacity. On hover the border goes fully white and the background picks up a faint white wash (8%).
- **Top-bar Contact:** a compact jade-filled version (8px 16px) at the right end of the top bar.
- **Copy-email row:** the email in mono joined to a text button inside one rule-2 box. The button is jade text and fills jade on hover.

### Chips / Tags
- **Style:** inline, uppercase label type, 1px border, square, 3px 7px padding.
- **State:** jade border and text for done states (filed, granted). Peach border and text for planned or target.

### Cards / Containers
There are no cards. Grouped content (pilots, team members, frequency bands) is separated by 1px vertical and horizontal rules on open ground, never set in a filled or rounded box.

### Inputs / Fields
- **Style:** transparent, a single 1px rule-2 bottom border, 0px radius, Manrope 17px. Labels sit above in uppercase label type in ink-3.
- **Hover:** the underline lightens to ink-3. **Focus:** the underline turns jade.
- **Error:** the form message turns peach. **Disabled:** the submit button drops to 55% opacity.

### Navigation
- **Top bar:** fixed, 60px, ground background, 1px rule bottom border, white logo on the left. Text links are Space Grotesk 500 at 14px in ink-2. On hover they turn ink with a jade 1px underline. The language switch is set in Manrope. Below 1100px only the language switch and Contact stay visible.
- **Stage rail:** fixed on the left from 1280px up. It is a 1px vertical rule with square 7px markers and uppercase label-type links in ink-3. The current stage turns jade, and its marker fills jade and scales to 1.3 (0.3s). It tracks the section in the middle of the viewport. Each rail link must match a section id on the page.

### Scene Frame (signature)
Every image sits in a frame: the image is cropped to the frame's aspect ratio (16:10 media, 21:9 bleed, 4:3 strips, 3:2 and 1:1 sheets) and has a 1px rule border (rule-2 on hero and bleed frames). Jade corner ticks draw in (fading from 1.02 scale over 0.9s, easing cubic-bezier(.16,1,.3,1)) when a quarter of the frame enters the viewport. Without JavaScript, or with reduced motion, the ticks are simply shown. A caption below in label type puts the image type (illustration, design render, from orbit) on the left and the subject in bold ink-2 on the right.

Photographs of events and people are muted by default: field and event photos at saturate 0.62, team portraits in greyscale, scenes on the contact sheet at saturate 0.9. They return to full colour on hover (0.4 to 0.5s).

### Metadata Collar (signature)
A row of four ruled cells pinned under the hero scene, on a 0.78 ground panel with rule-2 dividers. Each cell has a mono figure in ink over a one-line description at 13px in ink-2. A planned figure is peach. It goes 2-up under 760px.

### Ledger
A dated list of milestones in ruled rows: year in jade mono, title in Space Grotesk 500 at 18px, detail in ink-2, status in label type on the right. The current row has a jade top rule. Planned rows turn year and status peach. Hovering a row raises it to ground-2.

### Accepted exceptions
- **Round globe image:** the AgriEasy globe is a round, glossy infographic, kept at the owner's request. It sits centred inside a square ground-2 plate with a 1px rule border, so the square grammar holds around it. Don't use this as a precedent for round or glossy imagery elsewhere.
- **Full-width event photo:** the wide event photo in the team section (16:7, 4:3 on mobile) is full width at the owner's request. It still follows the frame, ticks, caption and muted-grade rules.

## Do's and Don'ts

### Do:
- **Do** put every image in a frame with corner ticks, a 1px border and a label-type caption giving the image type and subject.
- **Do** label renders, illustrations and representative images honestly in the caption ("Design render", "Illustration", "From orbit").
- **Do** keep peach for planned, target or not-yet-done states only (The Future Tense Rule).
- **Do** set measured values (counts, metres, years) in Geist Mono with tabular figures, and nothing else.
- **Do** build structure from 1px rules (rule, rule-2) and square corners (0px).
- **Do** keep the English and Chinese pages in step. Both are generated in matching pairs from `tools/build_pages.py`, so change both together, and regenerate rather than hand-editing one page.
- **Do** keep each stage rail link in step with a section id when you add or rename a section.
- **Do** apply the CJK heading override (0 tracking, looser leading) to any new heading style.

### Don't:
- **Don't** round corners, use pill-shaped navigation or buttons, or put content in filled, rounded cards.
- **Don't** add box-shadows, glows, or gradient blob backgrounds. Gradients are only scrims over images, in the ground colour.
- **Don't** use peach as a second accent, for decoration or for emphasis.
- **Don't** introduce new colours. The nine tokens in the frontmatter are the complete palette.
- **Don't** set text over an image without a ground scrim or a ground panel behind it.
- **Don't** add small uppercase labels above headings. Label type belongs in captions, tables, tags, the rail and the scene ID, not as a lead-in to a heading.
- **Don't** use icon fonts or emoji. Icons are inline SVG line arrows at a 1.4 stroke weight in currentColor.
