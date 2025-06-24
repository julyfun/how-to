## Pipeline 的职责是?

pipe:
- unet
- vae
- text_encoder
- image_encoder
- feature_extractor
- tokenizer (is a nn.Module without params)
- scheduler
- safety_checker ?
