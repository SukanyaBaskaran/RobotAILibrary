from huggingface_hub import snapshot_download

# ✅ Downloads full DeepSeek-V3 model
snapshot_download(repo_id="deepseek-ai/DeepSeek-V3-Base", local_dir="DeepSeek-V3-Base")