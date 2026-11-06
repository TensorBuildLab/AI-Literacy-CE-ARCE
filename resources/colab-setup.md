# Google Colab Setup Guide

All labs run in **Google Colab**: Python notebooks in your web browser, free, nothing to install.

## One-time setup (5 minutes, before Lab 01)
1. Use a laptop with Chrome, Edge, Firefox, or Safari. A tablet is not enough for labs.
2. Go to <https://colab.research.google.com> and sign in with a Google account. **Any Google account works (personal or university) — use the same one all semester** so your saved copies stay in one Google Drive.
3. Click **New notebook**, type `print("hello")` in the grey cell, and press **Shift + Enter**. If you see `hello`, you're ready.

## Opening a lab notebook
1. On the [course home page](../README.md), click the lab (for example, *Lab 01 — Python On-Ramp*).
2. Click the **Open in Colab** badge.
3. Colab may warn: *"This notebook was not authored by Google."* That's normal for course notebooks — click **Run anyway**.
4. **Immediately** choose **File → Save a copy in Drive.** Work only in your copy (its title starts with "Copy of"). Otherwise your work is not saved.

## Running cells
- **Shift + Enter** runs the current cell and moves to the next one.
- Run cells **in order, top to bottom.** A notebook remembers what you ran, not what's above on the page.
- `[*]` next to a cell means it is still running. `[5]` means it was the 5th cell run.
- **Runtime → Run all** runs everything; **Runtime → Run before** runs everything above the current cell.
- **Runtime → Restart session** clears memory. Then re-run from the top.

## Internet and data use
Colab runs on Google's computers. When a lab downloads a model (often 0.5–1 GB), the download happens **on Google's side — it does not use your laptop storage or your phone's data plan**. Your own connection only carries the web page. Videos in the weekly readings are what use your data: choose 480p or use campus Wi-Fi.

## Turning off AI suggestions (for AI-Free work)
Colab can suggest code with AI as you type. For AI-Free work, open **Tools → Settings → AI assistance** and turn off the AI-powered completions. (Menu names change; ask if you can't find it.)

## GPU runtime (optional: Labs 06, 08, 10, 13 run faster with it)
**Runtime → Change runtime type → T4 GPU → Save.** Free GPU time is limited each day; if Colab says no GPU is available, every lab still works on the default CPU runtime, just more slowly. Switch back to CPU when you don't need it.

## Submitting
Labs are due **Sunday 11:59 pm (Arizona time)** at the end of the lab's week.
1. **Runtime → Restart session and run all.** Fix anything that fails. (Labs that load a model take a few extra minutes to re-run; in Lab 10, type `no` if the approval box appears.)
2. **File → Download → Download .ipynb**.
3. Upload that file to the matching assignment on **Brightspace**.

## Troubleshooting
| Problem | Fix |
|---|---|
| `NameError: name 'x' is not defined` | You skipped a cell above. **Runtime → Run before**, then run the cell again. |
| `ModuleNotFoundError` | Re-run the setup cell (and any `!pip install` cell) at the top of the notebook. |
| Data download fails (`HTTPError`) | Check your internet connection and re-run. If it keeps failing, download the file from the course `data/` folder and upload it with the 📁 **Files** panel on the left. |
| "Your session crashed after using all available RAM" | **Runtime → Restart session**, then run cells in order. Delete models you no longer need (`del model`). |
| Very slow model download | The first download takes 1–3 minutes; later runs in the same session are fast. |
| Colab disconnected after being idle | Reconnect, then re-run from the top (your code is still there; variables are not). |
| Lost my work | Did you use **File → Save a copy in Drive**? Check **File → Open notebook → Google Drive** for "Copy of …". |

## Running notebooks on your own computer (optional)
Install [Anaconda](https://www.anaconda.com), then `pip install torch torchvision transformers scikit-learn pandas matplotlib`. Open the notebook in Jupyter. The `get_data()` helper in each notebook downloads course data automatically. Colab-only cells (marked *optional*) can be skipped.
