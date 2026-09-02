# Cooking Reel — Production Plan (auto-resume state)

Instagram-ready vertical (9:16) cooking reel: **"5-Minute Viral Cucumber–Avocado–Feta Salad"**,
featuring the creator's own face (2 face shots: hook + outro; rest is hands/food b-roll).

**Status:** BLOCKED on Higgsfield credits (balance 0 on Plus plan, Private workspace).
Monthly 1,000-credit grant renews ~Sept 9. A top-up unblocks immediately.
This session self-checks the balance on a schedule and runs the pipeline automatically once credits land.

## Confirmed Higgsfield media (already uploaded)

- Face ref A (clear face, evening, black dress): media_id `6af61823-ab17-40c0-b0d4-0d2c3f46c65d`
- Face ref B (car selfie, sunglasses, blue striped sweater — outfit ref): media_id `f3404ae0-9b8c-4146-a7fd-9128b803d452`

## Budget (get_cost verified)

- Keyframe image (nano_banana_pro, 2k, 9:16): 2 cr each
- Video 5s 9:16: seedance_2_0 std 1080p = 45 cr; seedance_2_0_mini 720p = 12.5 cr
- Voiceover (seed_audio): ~1–2 cr
- Plan A (balance ≥ 420): 7 keyframes (14) + 7 clips @45 (315) + VO (2) + retake margin ≈ 400
- Plan B (balance ≥ 160): 2 face clips @45 + 5 b-roll @12.5 + images + VO ≈ 170 + margin
- Plan C (balance ≥ 110): all clips mini 720p ≈ 105 + margin, upscale later if desired

## Shot list (7 × 5s → final ~30s)

1. HOOK (face): she stands at kitchen island, holds cucumber near face, talks to camera, natural smile.
2. Hands chopping cucumber into thin half-moons on wooden board (close-up, no face).
3. Halving cherry tomatoes + dicing avocado into glass bowl (close-up).
4. Crumbling feta + scattering thin red onion over the bowl (top-down).
5. Dressing: olive oil drizzle, lemon squeeze, salt + chili flakes (macro).
6. Big toss of the colorful salad in the glass bowl.
7. OUTRO (face): she tastes a forkful, happy nod/smile to camera.

Continuity lock: bright modern kitchen, white quartz island, light oak cabinets, morning window light,
wooden board, glass bowl, light blue crewneck sweater w/ thin dark stripes (from face ref B), gold necklace.

## Pipeline (run when credits available)

1. Keyframe 1 via `generate_image_batch` nano_banana_pro 9:16, medias image_references = [face A, face B].
   Check likeness from result URL. Then keyframes 2–7 in one batch, each referencing keyframe-1 job_id
   (kitchen/outfit continuity) + face A for the two face shots.
2. Clips via `generate_video_batch`, start_image = keyframe job_id, 5s, 9:16, native audio ON
   (ambient kitchen sounds; NO speech in prompts — VO is separate). Model per budget plan above.
3. VO via `generate_audio` seed_audio, voice_type preset, voice_id `7367e919-3069-5a0b-939e-dfb1c0fd91b4` (Isla; fallback Kaia `bb9db352-f345-59f3-90b3-fa9432bcff91`), speech_rate +8.
4. Assemble in Higgsfield `sandbox_exec` (ffmpeg): trim each clip ~4.2s, concat, duck ambient under VO,
   loudness normalize, 1080x1920 H.264 + AAC. Export two versions:
   - `salad_reel_voiceover.mp4` (VO + ambient)
   - `salad_reel_clean.mp4` (ambient only — for trending audio in the IG app)
   Upload both via `media_upload` from sandbox, `media_confirm`, download locally,
   deliver via SendUserFile and commit to this branch under `cooking-reel/`.

## Voiceover script (~28s, casual creator tone)

"Okay — this is the viral cucumber feta salad everyone's making, and it takes five minutes.
Chop up two cucumbers, nice and thin. Throw in cherry tomatoes... and a whole avocado.
Then crumble in way too much feta — that's the rule. Olive oil, fresh lemon, salt, chili flakes.
Give it a big toss... and that's it. Creamy, crunchy, ridiculously good. Save this for lunch this week."
