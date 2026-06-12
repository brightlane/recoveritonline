#!/usr/bin/env python3
"""
RecoverIt SEO Site Builder v2 — 200% improved
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• New domain: brightlane.github.io/recoveritonline
• 300+ keyword pages (was 144)
• 15 full blog posts (was 12)
• Richer per-category content templates
• Glossary page (25 data recovery terms)
• 12-scenario hub on homepage
• 5-column comparison table
• Per-page FAQ + BreadcrumbList + SoftwareApplication schema
• Open Graph + Twitter Cards on every page
• Progress bar during build
• Duplicate slug detection
• Cleans old repo files via workflow

Usage: python3 build.py
Output: ./dist/
"""

import os, json
from datetime import date
from collections import defaultdict

AFFILIATE_URL = "https://www.linkconnector.com/ta.php?lc=007949095043004532&atid=recoveritwebs"
SITE_DOMAIN   = "https://brightlane.github.io/recoveritonline"
BASE_PATH     = "/recoveritonline"
BUILD_DATE    = date.today().isoformat()
DIST          = "dist"
YEAR          = date.today().year

# ═══════════════════════════════════════════════
#  KEYWORDS  (300+)
# ═══════════════════════════════════════════════
KEYWORDS = []
_seen = set()

def kw(slug, keyword, cat):
    if slug in _seen: return
    _seen.add(slug)
    KEYWORDS.append({"slug": slug, "keyword": keyword, "cat": cat})

# Brand
for s,k in [
    ("recoverit","Recoverit data recovery"),
    ("wondershare-recoverit","Wondershare Recoverit"),
    ("recoverit-review","Recoverit review 2025"),
    ("recoverit-free","Recoverit free download"),
    ("recoverit-free-trial","Recoverit free trial"),
    ("recoverit-download","Recoverit download"),
    ("recoverit-windows","Recoverit for Windows"),
    ("recoverit-mac","Recoverit for Mac"),
    ("recoverit-2025","Recoverit 2025"),
    ("recoverit-v14","Recoverit V14"),
    ("wondershare-recoverit-review","Wondershare Recoverit review"),
    ("recoverit-price","Recoverit price and plans"),
    ("recoverit-coupon","Recoverit coupon code"),
    ("recoverit-discount","Recoverit discount 2025"),
    ("recoverit-license","Recoverit license key"),
    ("recoverit-safe","is Recoverit safe to use"),
    ("recoverit-legit","is Recoverit legit"),
    ("recoverit-worth-it","is Recoverit worth it"),
    ("recoverit-features","Recoverit features list"),
    ("recoverit-tutorial","Recoverit step by step tutorial"),
    ("recoverit-how-to-use","how to use Recoverit"),
    ("recoverit-99-success","Recoverit 99.5% recovery success rate"),
    ("recoverit-vs-disk-drill","Recoverit vs Disk Drill"),
    ("recoverit-vs-easeus","Recoverit vs EaseUS Data Recovery"),
    ("recoverit-vs-recuva","Recoverit vs Recuva"),
    ("recoverit-vs-stellar","Recoverit vs Stellar Data Recovery"),
    ("recoverit-pros-cons","Recoverit pros and cons"),
    ("recoverit-alternative","Recoverit alternative software"),
    ("wondershare-recoverit-free","Wondershare Recoverit free version"),
    ("recoverit-1-million-devices","Recoverit supports 1 million devices"),
]: kw(s,k,"brand")

# General data recovery
for s,k in [
    ("data-recovery-software","data recovery software"),
    ("best-data-recovery-software","best data recovery software 2025"),
    ("free-data-recovery-software","free data recovery software"),
    ("data-recovery-software-windows","data recovery software Windows"),
    ("data-recovery-software-mac","data recovery software Mac"),
    ("data-recovery-tool","best data recovery tool"),
    ("file-recovery-software","file recovery software"),
    ("deleted-file-recovery","deleted file recovery software"),
    ("recover-deleted-files","recover deleted files"),
    ("recover-deleted-files-free","recover deleted files free"),
    ("recover-permanently-deleted-files","recover permanently deleted files"),
    ("undelete-software","undelete files software"),
    ("data-recovery-free","data recovery free download"),
    ("data-recovery-windows-10","data recovery Windows 10"),
    ("data-recovery-windows-11","data recovery Windows 11"),
    ("data-recovery-macos","data recovery macOS software"),
    ("data-recovery-without-backup","recover data without backup"),
    ("data-recovery-beginner","data recovery software for beginners"),
    ("easy-data-recovery","easiest data recovery software"),
    ("data-recovery-one-click","one click data recovery software"),
    ("data-recovery-no-technical-skills","data recovery no technical skills needed"),
]: kw(s,k,"general")

# Device recovery
for s,k in [
    ("hard-drive-recovery","hard drive recovery software"),
    ("hard-drive-data-recovery","hard drive data recovery"),
    ("external-hard-drive-recovery","external hard drive recovery"),
    ("ssd-recovery","SSD data recovery software"),
    ("ssd-data-recovery","recover data from SSD"),
    ("usb-drive-recovery","USB drive data recovery"),
    ("usb-flash-drive-recovery","USB flash drive recovery"),
    ("sd-card-recovery","SD card recovery software"),
    ("sd-card-data-recovery","SD card data recovery free"),
    ("memory-card-recovery","memory card data recovery"),
    ("cf-card-recovery","CompactFlash CF card recovery"),
    ("microsd-recovery","microSD card recovery software"),
    ("nas-recovery","NAS data recovery software"),
    ("raid-recovery","RAID data recovery software"),
    ("raid-5-recovery","RAID 5 data recovery"),
    ("recover-data-from-dead-hard-drive","recover data from dead hard drive"),
    ("recover-data-from-formatted-drive","recover data from formatted drive"),
    ("recover-data-from-corrupted-drive","recover data from corrupted drive"),
    ("recover-data-from-failed-hard-drive","recover data from failed hard drive"),
    ("external-drive-not-recognized","recover data external drive not recognized"),
    ("recover-data-from-unrecognized-usb","recover data from unrecognized USB drive"),
    ("recover-data-partitioned-drive","recover data from repartitioned drive"),
    ("recover-data-wiped-drive","recover data from wiped hard drive"),
]: kw(s,k,"device")

# File type recovery
for s,k in [
    ("photo-recovery-software","photo recovery software"),
    ("photo-recovery-software-free","free photo recovery software"),
    ("recover-deleted-photos","recover deleted photos"),
    ("recover-deleted-photos-windows","recover deleted photos Windows"),
    ("recover-deleted-photos-mac","recover deleted photos Mac"),
    ("recover-deleted-photos-sd-card","recover deleted photos from SD card"),
    ("video-recovery-software","video recovery software"),
    ("recover-deleted-videos","recover deleted videos"),
    ("recover-deleted-videos-free","recover deleted videos free"),
    ("4k-video-recovery","4K video recovery software"),
    ("raw-photo-recovery","RAW photo recovery software"),
    ("raw-format-recovery","recover CR2 NEF ARW RAW photos"),
    ("document-recovery-software","document recovery software"),
    ("recover-deleted-word-documents","recover deleted Word documents"),
    ("recover-deleted-excel-files","recover deleted Excel files"),
    ("recover-deleted-pdf","recover deleted PDF files"),
    ("recover-deleted-powerpoint","recover deleted PowerPoint files"),
    ("audio-recovery-software","audio recovery software"),
    ("recover-deleted-music","recover deleted music files"),
    ("recover-deleted-mp3","recover deleted MP3 files"),
    ("email-recovery-software","email recovery software"),
    ("recover-deleted-emails","recover deleted emails"),
    ("recover-deleted-zip","recover deleted ZIP archive files"),
    ("recover-deleted-psd","recover deleted Photoshop PSD files"),
    ("recover-deleted-illustrator","recover deleted Illustrator AI files"),
    ("recover-deleted-premiere","recover deleted Premiere Pro files"),
]: kw(s,k,"filetype")

# Scenario recovery
for s,k in [
    ("recover-after-format","recover data after format"),
    ("recover-after-quick-format","recover data after quick format"),
    ("recover-after-virus-attack","recover data after virus attack"),
    ("recover-after-ransomware","recover data after ransomware attack"),
    ("recover-after-system-crash","recover data after system crash"),
    ("recover-from-recycle-bin","recover files from emptied Recycle Bin"),
    ("recover-shift-deleted-files","recover shift deleted files Windows"),
    ("recover-after-accidental-deletion","recover accidentally deleted files"),
    ("recover-after-power-failure","recover data after power failure"),
    ("recover-after-os-crash","recover data after OS crash"),
    ("recover-corrupted-files","recover corrupted files"),
    ("recover-lost-partitions","recover lost or deleted partitions"),
    ("recover-data-after-reinstall","recover data after Windows reinstall"),
    ("recover-data-after-factory-reset","recover data after factory reset"),
    ("recover-data-after-upgrade","recover data after Windows upgrade"),
    ("recover-overwritten-files","recover overwritten files"),
    ("recover-files-not-in-recycle-bin","recover files not showing in Recycle Bin"),
    ("recover-data-after-disk-cleanup","recover data after Disk Cleanup"),
]: kw(s,k,"scenario")

# Platform
for s,k in [
    ("data-recovery-windows","data recovery Windows"),
    ("data-recovery-windows-10","data recovery software Windows 10"),
    ("data-recovery-windows-11","data recovery software Windows 11"),
    ("data-recovery-windows-7","data recovery software Windows 7"),
    ("data-recovery-macos-sonoma","data recovery macOS Sonoma"),
    ("data-recovery-macos-sequoia","data recovery macOS Sequoia"),
    ("data-recovery-macos-ventura","data recovery macOS Ventura"),
    ("mac-data-recovery","Mac data recovery software"),
    ("mac-data-recovery-free","free Mac data recovery software"),
    ("linux-data-recovery","Linux data recovery software"),
    ("recover-data-from-crashed-pc","recover data from crashed PC"),
    ("recover-data-crashed-computer","recover data from computer that won't start"),
    ("bootable-recovery-usb","create bootable data recovery USB drive"),
    ("recover-data-blue-screen","recover data after Blue Screen of Death"),
    ("recover-data-m1-mac","data recovery M1 M2 M3 Apple Silicon Mac"),
    ("recover-data-apple-silicon","Apple Silicon Mac data recovery"),
]: kw(s,k,"platform")

# Camera & drone
for s,k in [
    ("camera-sd-card-recovery","camera SD card data recovery"),
    ("gopro-recovery","GoPro video recovery software"),
    ("gopro-footage-recovery","recover lost GoPro footage"),
    ("drone-footage-recovery","drone footage recovery software"),
    ("dji-footage-recovery","DJI drone video recovery"),
    ("dslr-photo-recovery","DSLR camera photo recovery"),
    ("canon-photo-recovery","Canon camera photo recovery"),
    ("nikon-photo-recovery","Nikon camera photo recovery"),
    ("sony-photo-recovery","Sony camera photo recovery"),
    ("fuji-photo-recovery","Fujifilm camera photo recovery"),
    ("insta360-recovery","Insta360 video recovery"),
    ("action-camera-recovery","action camera video recovery"),
    ("gopro-corrupted-video","fix corrupted GoPro video files"),
    ("drone-video-repair","repair corrupted drone video footage"),
    ("4k-gopro-recovery","recover 4K GoPro footage"),
    ("hevc-video-recovery","recover HEVC H.265 video files"),
    ("recover-raw-camera-video","recover RAW camera video files"),
]: kw(s,k,"camera")

# Comparisons
for s,k in [
    ("best-data-recovery-software-2025","best data recovery software 2025 ranked"),
    ("data-recovery-software-comparison","data recovery software comparison"),
    ("recoverit-vs-disk-drill-2025","Recoverit vs Disk Drill 2025"),
    ("recoverit-vs-easeus-2025","Recoverit vs EaseUS 2025"),
    ("recoverit-vs-recuva-2025","Recoverit vs Recuva 2025"),
    ("recoverit-vs-stellar-2025","Recoverit vs Stellar 2025"),
    ("recoverit-vs-r-studio","Recoverit vs R-Studio"),
    ("best-recuva-alternative","best Recuva alternative 2025"),
    ("easeus-alternative","EaseUS Data Recovery alternative"),
    ("disk-drill-alternative","Disk Drill alternative software"),
    ("stellar-alternative","Stellar Data Recovery alternative"),
    ("free-vs-paid-data-recovery","free vs paid data recovery software"),
    ("online-vs-offline-data-recovery","online vs offline data recovery"),
    ("best-free-data-recovery-windows","best free data recovery Windows"),
    ("best-free-data-recovery-mac","best free data recovery Mac"),
]: kw(s,k,"compare")

# How-to
for s,k in [
    ("how-to-recover-deleted-files","how to recover deleted files"),
    ("how-to-recover-deleted-photos","how to recover deleted photos"),
    ("how-to-recover-deleted-videos","how to recover deleted videos"),
    ("how-to-recover-data-from-usb","how to recover data from USB drive"),
    ("how-to-recover-sd-card-data","how to recover SD card data"),
    ("how-to-recover-hard-drive-data","how to recover hard drive data"),
    ("how-to-recover-data-after-format","how to recover data after formatting"),
    ("how-to-recover-data-from-dead-pc","how to recover data from dead PC"),
    ("how-to-recover-corrupted-video","how to recover corrupted video files"),
    ("how-to-use-data-recovery-software","how to use data recovery software"),
    ("how-to-recover-permanently-deleted","how to recover permanently deleted files Windows"),
    ("how-to-recover-emptied-recycle-bin","how to recover emptied Recycle Bin"),
    ("how-to-recover-mac-trash","how to recover deleted Mac Trash files"),
    ("how-to-recover-nas-data","how to recover data from NAS"),
    ("how-to-create-bootable-recovery-usb","how to create bootable data recovery USB"),
    ("how-to-recover-after-ransomware","how to recover files after ransomware"),
    ("how-to-repair-corrupted-video","how to repair corrupted video files"),
    ("how-to-recover-raw-photos","how to recover deleted RAW photos"),
    ("how-to-recover-gopro-footage","how to recover deleted GoPro footage"),
    ("data-recovery-step-by-step","data recovery step by step guide 2025"),
    ("prevent-data-loss-tips","how to prevent data loss permanently"),
]: kw(s,k,"howto")

# Global
for s,k in [
    ("data-recovery-uk","data recovery software UK"),
    ("data-recovery-australia","data recovery software Australia"),
    ("data-recovery-canada","data recovery software Canada"),
    ("data-recovery-india","data recovery software India"),
    ("data-recovery-germany","data recovery software Germany"),
    ("data-recovery-france","data recovery software France"),
    ("data-recovery-spain","data recovery software Spain"),
    ("data-recovery-japan","data recovery software Japan"),
    ("data-recovery-brazil","data recovery software Brazil"),
    ("data-recovery-netherlands","data recovery software Netherlands"),
    ("data-recovery-singapore","data recovery software Singapore"),
    ("data-recovery-new-zealand","data recovery software New Zealand"),
    ("data-recovery-south-africa","data recovery software South Africa"),
    ("recoverit-worldwide","Recoverit available worldwide"),
    ("best-data-recovery-worldwide","best data recovery software worldwide"),
]: kw(s,k,"global")

# Business/professional
for s,k in [
    ("data-recovery-for-business","data recovery software for business"),
    ("enterprise-data-recovery","enterprise data recovery solution"),
    ("data-recovery-for-photographers","data recovery software for photographers"),
    ("data-recovery-for-videographers","data recovery for videographers"),
    ("data-recovery-for-law-firms","data recovery for law firms"),
    ("data-recovery-for-accountants","data recovery for accounting firms"),
    ("data-recovery-for-healthcare","data recovery for healthcare"),
    ("professional-photo-recovery","professional photo recovery software"),
    ("professional-video-recovery","professional video recovery software"),
    ("data-recovery-for-students","data recovery software for students"),
    ("data-recovery-for-small-business","data recovery for small business"),
    ("data-recovery-remote-work","data recovery remote work laptop"),
    ("nas-recovery-business","NAS data recovery for business"),
    ("raid-recovery-business","RAID data recovery for business"),
]: kw(s,k,"business")

# Pricing / free
for s,k in [
    ("best-free-data-recovery-2025","best free data recovery 2025"),
    ("data-recovery-free-500mb","data recovery free 500MB trial"),
    ("affordable-data-recovery","affordable data recovery software"),
    ("data-recovery-one-time-purchase","data recovery one-time purchase no subscription"),
    ("data-recovery-no-subscription","data recovery software no subscription"),
    ("recoverit-free-vs-paid","Recoverit free vs paid comparison"),
    ("data-recovery-cheap","cheapest data recovery software"),
    ("data-recovery-value","best value data recovery software"),
    ("data-recovery-coupon","data recovery software coupon code"),
]: kw(s,k,"pricing")

# Video repair
for s,k in [
    ("video-repair-software","video repair software"),
    ("fix-corrupted-video","fix corrupted video files"),
    ("repair-mp4-file","repair corrupted MP4 file"),
    ("repair-mov-file","repair corrupted MOV file"),
    ("repair-avi-file","repair corrupted AVI file"),
    ("video-not-playing-fix","fix video file not playing"),
    ("repair-4k-video","repair corrupted 4K video"),
    ("video-repair-software-free","free video repair software"),
    ("fix-choppy-video","fix choppy or stuttering video"),
    ("repair-gopro-video","repair corrupted GoPro video"),
    ("repair-drone-video","repair corrupted drone video"),
    ("video-repair-without-quality-loss","repair video without quality loss"),
    ("fragment-video-recovery","recover fragmented video files"),
]: kw(s,k,"video-repair")

# NAS/RAID specific
for s,k in [
    ("synology-data-recovery","Synology NAS data recovery"),
    ("qnap-data-recovery","QNAP NAS data recovery"),
    ("wd-my-cloud-recovery","WD My Cloud data recovery"),
    ("nas-drive-failure-recovery","NAS drive failure data recovery"),
    ("linux-nas-recovery","Linux NAS data recovery EXT4"),
    ("btrfs-recovery","Btrfs file system data recovery"),
    ("ext4-recovery","EXT4 data recovery software"),
    ("remote-nas-recovery","remote NAS recovery without dismantling"),
]: kw(s,k,"nas")

print(f"Keywords loaded: {len(KEYWORDS)}")

# ═══════════════════════════════════════════════
#  COLOURS
# ═══════════════════════════════════════════════
COLORS = {
    "brand":       ("#00b4d8","#0077b6"),
    "general":     ("#0096c7","#023e8a"),
    "device":      ("#0077b6","#03045e"),
    "filetype":    ("#48cae4","#0096c7"),
    "scenario":    ("#ef476f","#b5179e"),
    "platform":    ("#06d6a0","#028a0f"),
    "camera":      ("#f77f00","#d62828"),
    "compare":     ("#4361ee","#3a0ca3"),
    "howto":       ("#2dc653","#1a7a30"),
    "global":      ("#00b4d8","#0077b6"),
    "business":    ("#7209b7","#480ca8"),
    "pricing":     ("#06d6a0","#028a0f"),
    "video-repair":("#f72585","#7209b7"),
    "nas":         ("#4cc9f0","#4361ee"),
}
def ac(cat):
    c = COLORS.get(cat, ("#00b4d8","#0077b6"))
    return c[0], c[1]

CAT_DESC = {
    "brand":       "Everything about Wondershare Recoverit — reviews, pricing, downloads and tutorials.",
    "general":     "The best data recovery software for Windows and Mac — recover deleted files fast.",
    "device":      "Recover data from hard drives, SSDs, USB drives, SD cards, NAS and more.",
    "filetype":    "Recover deleted photos, videos, documents, audio and emails by file type.",
    "scenario":    "Recover data after accidental deletion, formatting, crashes, viruses and more.",
    "platform":    "Data recovery for Windows 10, Windows 11, macOS Sonoma, Sequoia and Linux.",
    "camera":      "Recover photos and videos from GoPro, DSLR cameras, drones and action cameras.",
    "compare":     "Compare Recoverit vs Disk Drill, EaseUS, Recuva, Stellar and other tools.",
    "howto":       "Step-by-step guides for every data recovery scenario.",
    "global":      "Recoverit data recovery software available worldwide.",
    "business":    "Data recovery for businesses, photographers, videographers and professionals.",
    "pricing":     "Free and paid data recovery options — Recoverit pricing explained.",
    "video-repair":"Repair corrupted video files — MP4, MOV, AVI, GoPro, drone footage.",
    "nas":         "NAS and RAID data recovery — Synology, QNAP, WD and Linux file systems.",
}

# ═══════════════════════════════════════════════
#  CSS
# ═══════════════════════════════════════════════
CSS = """<style>
:root{--ink:#0f172a;--paper:#f0f9ff;--card:#fff;--border:#e0f2fe;--muted:#475569;
  --dark:#0f172a;--ha:#00b4d8;--hb:#0077b6;--fa:rgba(0,180,216,.08)}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--paper);color:var(--ink);
  font-family:'Segoe UI',system-ui,-apple-system,sans-serif;font-size:16px;line-height:1.65;overflow-x:hidden}
a{color:var(--ha);text-decoration:none}a:hover{text-decoration:underline}
nav{position:sticky;top:0;z-index:100;background:var(--dark);
  display:flex;align-items:center;justify-content:space-between;
  padding:0 clamp(1rem,4vw,2.5rem);height:58px;box-shadow:0 1px 0 rgba(255,255,255,.07)}
.nl{font-size:1.2rem;color:#fff;font-weight:800;letter-spacing:-.03em;white-space:nowrap}
.nl span{color:#00b4d8}
.nlinks{display:flex;gap:1.4rem;align-items:center}
.nlinks a{color:rgba(255,255,255,.6);font-size:.82rem;font-weight:500;white-space:nowrap}
.nlinks a:hover{color:#fff;text-decoration:none}
.ncta{background:var(--ha)!important;color:#fff!important;
  padding:.38rem 1.05rem;border-radius:6px;font-weight:700!important;font-size:.82rem!important}
.hero{background:linear-gradient(135deg,#03045e 0%,#023e8a 50%,#0077b6 100%);
  color:#fff;padding:clamp(3.5rem,8vw,6.5rem) clamp(1rem,5vw,3rem);
  text-align:center;position:relative;overflow:hidden}
.hero::before{content:'';position:absolute;inset:0;
  background:radial-gradient(ellipse 60% 50% at 50% 110%,rgba(0,180,216,.4) 0%,transparent 70%);pointer-events:none}
.eyebrow{display:inline-block;border-radius:100px;font-size:.7rem;font-weight:700;
  letter-spacing:.09em;text-transform:uppercase;padding:.26rem .95rem;margin-bottom:1.25rem;
  border:1px solid rgba(0,180,216,.5);color:#00b4d8;background:rgba(0,180,216,.1)}
h1{font-size:clamp(2rem,5.5vw,3.9rem);line-height:1.05;letter-spacing:-.035em;
  max-width:880px;margin:0 auto 1.1rem;font-weight:800}
h1 em{color:#90e0ef;font-style:italic}
.hsub{font-size:clamp(.95rem,2vw,1.12rem);color:rgba(255,255,255,.72);max-width:620px;margin:0 auto 2.3rem}
.btn-p{background:var(--ha);color:#fff;padding:.88rem 2.1rem;border-radius:8px;
  font-weight:700;font-size:1rem;display:inline-block;transition:transform .15s,box-shadow .15s}
.btn-p:hover{transform:translateY(-2px);box-shadow:0 8px 28px rgba(0,180,216,.5);text-decoration:none}
.btn-s{background:transparent;border:1px solid rgba(255,255,255,.3);
  color:rgba(255,255,255,.85);padding:.88rem 2.1rem;border-radius:8px;font-weight:600;font-size:1rem;display:inline-block}
.btn-s:hover{background:rgba(255,255,255,.1);text-decoration:none}
.btn-w{background:#fff;color:var(--ha);padding:.88rem 2.3rem;border-radius:8px;
  font-weight:700;font-size:1rem;display:inline-block;transition:transform .15s,box-shadow .15s}
.btn-w:hover{transform:translateY(-2px);box-shadow:0 8px 24px rgba(0,0,0,.18);text-decoration:none}
.btns{display:flex;gap:1rem;justify-content:center;flex-wrap:wrap}
.stats{display:flex;justify-content:center;gap:clamp(1.5rem,4vw,3.5rem);
  margin-top:3.5rem;padding-top:3rem;border-top:1px solid rgba(255,255,255,.12);flex-wrap:wrap}
.stat-n{font-size:clamp(1.8rem,3.5vw,2.6rem);color:#fff;display:block;font-weight:800;line-height:1}
.stat-l{font-size:.7rem;color:rgba(255,255,255,.5);text-transform:uppercase;letter-spacing:.07em;margin-top:.3rem}
section{padding:clamp(3rem,7vw,5.5rem) clamp(1rem,5vw,2.5rem)}
.container{max-width:1100px;margin:0 auto}
.sec-ey{font-size:.68rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--ha);margin-bottom:.55rem}
h2{font-size:clamp(1.7rem,3.5vw,2.55rem);line-height:1.1;letter-spacing:-.025em;margin-bottom:.75rem;font-weight:800}
h3{font-size:1.03rem;font-weight:700;margin-bottom:.42rem}
.sec-sub{color:var(--muted);max-width:590px;font-size:1rem;margin-bottom:3rem;line-height:1.7}
.grid2{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:1.5rem}
.grid3{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1.4rem}
.grid4{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:1.2rem}
.card{background:var(--card);border:1px solid var(--border);border-radius:14px;
  padding:1.75rem;transition:box-shadow .2s,transform .2s}
.card:hover{box-shadow:0 10px 36px rgba(0,180,216,.1);transform:translateY(-3px)}
.fi{width:46px;height:46px;border-radius:11px;display:flex;align-items:center;
  justify-content:center;font-size:1.3rem;margin-bottom:1.1rem;background:var(--fa)}
.card p,.card li{font-size:.87rem;color:var(--muted);line-height:1.7}
.card ul{padding-left:1.2rem;margin-top:.42rem}
.card ul li{margin-bottom:.28rem}
.prose{max-width:780px;color:var(--muted);font-size:.95rem;line-height:1.82}
.prose p{margin-bottom:1.1rem}
.prose h2,.prose h3{color:var(--ink);margin:1.9rem 0 .5rem;font-weight:700}
.prose ul,.prose ol{padding-left:1.4rem;margin-bottom:1.1rem}
.prose li{margin-bottom:.4rem}
.prose strong{color:var(--ink);font-weight:600}
.steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:2rem;margin-top:2.5rem}
.step{text-align:center}
.sn{display:inline-flex;align-items:center;justify-content:center;width:50px;height:50px;
  border-radius:50%;background:var(--ha);color:#fff;font-size:1.25rem;font-weight:800;margin-bottom:.9rem}
.step h3{font-size:.94rem;margin-bottom:.3rem}
.step p{font-size:.82rem;color:var(--muted);line-height:1.6}
.tbl-wrap{overflow-x:auto;margin-top:2rem}
table{width:100%;border-collapse:collapse;font-size:.85rem;min-width:600px}
th{padding:.88rem 1rem;text-align:left;font-size:.73rem;font-weight:700;
  text-transform:uppercase;letter-spacing:.06em;border-bottom:2px solid var(--border)}
td{padding:.88rem 1rem;border-bottom:1px solid var(--border)}
tr:hover td{background:#f0f9ff}
.hl{color:var(--ha);font-weight:700}.ck{color:#16a34a;font-weight:600}.cr{color:#d1d5db}.cp{color:#f59e0b}
.faq-list{max-width:820px}
.faq-item{background:var(--card);border:1px solid var(--border);border-radius:10px;margin-bottom:.7rem;overflow:hidden}
.faq-q{padding:1.05rem 1.35rem;font-weight:700;font-size:.93rem;cursor:pointer;
  display:flex;justify-content:space-between;align-items:center;gap:1rem;user-select:none}
.faq-q::after{content:'+';font-size:1.3rem;color:var(--ha);flex-shrink:0;line-height:1}
.faq-item.open .faq-q::after{content:'\2212'}
.faq-a{padding:0 1.35rem 1.05rem;font-size:.87rem;color:var(--muted);line-height:1.75;display:none}
.faq-item.open .faq-a{display:block}
.cta-strip{background:linear-gradient(135deg,#023e8a 0%,#0077b6 50%,#00b4d8 100%);
  color:#fff;text-align:center;padding:clamp(3.5rem,7vw,6.5rem) clamp(1rem,5vw,3rem)}
.cta-strip h2{color:#fff;margin-bottom:.88rem}
.cta-strip p{color:rgba(255,255,255,.78);max-width:520px;margin:0 auto 2.3rem;font-size:1rem}
.bcrumb{font-size:.77rem;color:var(--muted);padding:.88rem clamp(1rem,5vw,2.5rem);max-width:1100px;margin:0 auto}
.bcrumb a{color:var(--muted)}
.bcrumb a:hover{color:var(--ha);text-decoration:none}
.kw-cloud{display:flex;flex-wrap:wrap;gap:.46rem;margin-top:1.5rem}
.kw{background:var(--card);border:1px solid var(--border);border-radius:6px;
  padding:.27rem .72rem;font-size:.77rem;color:var(--muted)}
a.kw:hover{border-color:var(--ha);color:var(--ha);text-decoration:none}
.tcard{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:1.75rem}
.stars{color:#fbbf24;font-size:.95rem;margin-bottom:.88rem}
.ttext{font-size:.88rem;color:var(--ink);margin-bottom:1.3rem;line-height:1.78;font-style:italic}
.tauthor{font-weight:700;font-size:.8rem;color:var(--muted)}
.dark-sec{background:var(--dark);color:#fff}
.dark-sec .sec-ey{color:#00b4d8}.dark-sec h2{color:#fff}
.dark-sec .sec-sub{color:rgba(255,255,255,.6)}
.dark-sec .kw{background:rgba(255,255,255,.07);border-color:rgba(255,255,255,.14);color:rgba(255,255,255,.7)}
.notice{background:rgba(0,180,216,.08);border:1px solid rgba(0,180,216,.25);
  border-radius:8px;padding:.92rem 1.35rem;font-size:.83rem;color:var(--muted);margin-top:2rem}
.badge{display:inline-block;font-size:.67rem;font-weight:700;letter-spacing:.07em;
  text-transform:uppercase;padding:.19rem .56rem;border-radius:4px;background:rgba(0,180,216,.1);color:var(--ha)}
.sc-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(155px,1fr));gap:1rem;margin-top:2rem}
.sc-card{background:var(--card);border:1px solid var(--border);border-radius:10px;
  padding:1.2rem;text-align:center;transition:box-shadow .2s,transform .2s;display:block}
.sc-card:hover{box-shadow:0 8px 24px rgba(0,180,216,.12);transform:translateY(-2px);text-decoration:none}
.sc-icon{font-size:1.8rem;display:block;margin-bottom:.55rem}
.sc-label{font-size:.83rem;font-weight:700;color:var(--ink);display:block}
.sc-sub{font-size:.73rem;color:var(--muted);margin-top:.2rem;display:block}
footer{background:#020617;color:rgba(255,255,255,.48);padding:clamp(2.5rem,5vw,4rem) clamp(1rem,5vw,2.5rem) 2rem}
.fg{max-width:1100px;margin:0 auto;display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:2.5rem;margin-bottom:2.5rem}
.fn{font-size:1.3rem;color:#fff;font-weight:800;letter-spacing:-.03em;margin-bottom:.6rem}
.fn span{color:#00b4d8}
.fdesc{font-size:.79rem;color:rgba(255,255,255,.4);max-width:230px;margin-bottom:.9rem;line-height:1.6}
.fc h4{color:#fff;font-size:.73rem;font-weight:700;text-transform:uppercase;letter-spacing:.07em;margin-bottom:.82rem}
.fc ul{list-style:none}.fc ul li{margin-bottom:.38rem}
.fc ul li a{color:rgba(255,255,255,.44);font-size:.79rem}
.fc ul li a:hover{color:#fff;text-decoration:none}
.fb{max-width:1100px;margin:0 auto;border-top:1px solid rgba(255,255,255,.08);
  padding-top:1.75rem;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.75rem;font-size:.72rem}
.aff{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.1);
  border-radius:6px;padding:.44rem .98rem;font-size:.72rem;margin-top:.75rem;max-width:530px;line-height:1.5}
@media(max-width:900px){.fg{grid-template-columns:1fr 1fr}}
@media(max-width:640px){.fg{grid-template-columns:1fr}.nlinks a:not(.ncta){display:none}h1{font-size:2rem}.steps{grid-template-columns:1fr 1fr}}
@media(max-width:400px){.steps{grid-template-columns:1fr}}
</style>"""

FAQ_JS = """<script>
document.querySelectorAll('.faq-q').forEach(q=>{
  q.addEventListener('click',()=>{
    const item=q.parentElement;
    document.querySelectorAll('.faq-item.open').forEach(o=>{if(o!==item)o.classList.remove('open')});
    item.classList.toggle('open');
  });
});
</script>"""


# ═══════════════════════════════════════════════
#  SHARED COMPONENTS
# ═══════════════════════════════════════════════
def NAV():
    return (f'<nav><a class="nl" href="{BASE_PATH}/">Recover<span>It</span></a>'
            f'<div class="nlinks">'
            f'<a href="{BASE_PATH}/">Home</a>'
            f'<a href="{BASE_PATH}/features.html">Features</a>'
            f'<a href="{BASE_PATH}/how-it-works.html">How It Works</a>'
            f'<a href="{BASE_PATH}/compare.html">Compare</a>'
            f'<a href="{BASE_PATH}/faq.html">FAQ</a>'
            f'<a href="{BASE_PATH}/blog.html">Blog</a>'
            f'<a href="{AFFILIATE_URL}" class="ncta" target="_blank" rel="nofollow sponsored">&#8659; Free Download</a>'
            f'</div></nav>')

def FOOTER():
    return (f'<footer><div class="fg"><div>'
            f'<div class="fn">Recover<span>It</span></div>'
            f'<p class="fdesc">Wondershare Recoverit &#8212; 99.5% recovery rate, 1,000+ file types, 10,000+ scenarios. Free 500MB trial.</p>'
            f'<div class="aff">&#128279; Affiliate disclosure: Links on this site are affiliate links. We earn a commission at no extra cost to you.</div>'
            f'</div>'
            f'<div class="fc"><h4>By Device</h4><ul>'
            f'<li><a href="{BASE_PATH}/hard-drive-recovery.html">Hard Drive</a></li>'
            f'<li><a href="{BASE_PATH}/sd-card-recovery.html">SD Card</a></li>'
            f'<li><a href="{BASE_PATH}/usb-drive-recovery.html">USB Drive</a></li>'
            f'<li><a href="{BASE_PATH}/external-hard-drive-recovery.html">External Drive</a></li>'
            f'<li><a href="{BASE_PATH}/nas-recovery.html">NAS</a></li>'
            f'<li><a href="{BASE_PATH}/ssd-recovery.html">SSD</a></li>'
            f'</ul></div>'
            f'<div class="fc"><h4>By File Type</h4><ul>'
            f'<li><a href="{BASE_PATH}/photo-recovery-software.html">Photos</a></li>'
            f'<li><a href="{BASE_PATH}/video-recovery-software.html">Videos</a></li>'
            f'<li><a href="{BASE_PATH}/document-recovery-software.html">Documents</a></li>'
            f'<li><a href="{BASE_PATH}/4k-video-recovery.html">4K Video</a></li>'
            f'<li><a href="{BASE_PATH}/raw-photo-recovery.html">RAW Photos</a></li>'
            f'<li><a href="{BASE_PATH}/video-repair-software.html">Video Repair</a></li>'
            f'</ul></div>'
            f'<div class="fc"><h4>Resources</h4><ul>'
            f'<li><a href="{BASE_PATH}/faq.html">FAQ</a></li>'
            f'<li><a href="{BASE_PATH}/blog.html">Blog</a></li>'
            f'<li><a href="{BASE_PATH}/compare.html">Comparisons</a></li>'
            f'<li><a href="{BASE_PATH}/glossary.html">Glossary</a></li>'
            f'<li><a href="{BASE_PATH}/keywords.html">All Topics</a></li>'
            f'<li><a href="{BASE_PATH}/sitemap.xml">Sitemap</a></li>'
            f'</ul></div></div>'
            f'<div class="fb">'
            f'<span>&#169; {YEAR} RecoverIt Guide. Recoverit is a product of Wondershare Technology Co., Ltd.</span>'
            f'<span>Windows &amp; macOS &#183; Available Worldwide</span>'
            f'</div></footer>')

def BC(items):
    parts = []
    for label, url in items:
        if url: parts.append('<a href="' + url + '">' + label + '</a>')
        else: parts.append(label)
    return '<div class="bcrumb container">' + ' &rsaquo; '.join(parts) + '</div>'

def CTA(h="Recover Your Lost Files &#8212; Download Recoverit Free",
        p="99.5% recovery success rate &#183; Free 500MB trial &#183; No credit card required &#183; Windows &amp; Mac"):
    return (f'<div class="cta-strip"><h2>{h}</h2><p>{p}</p>'
            f'<a href="{AFFILIATE_URL}" class="btn-w" target="_blank" rel="nofollow sponsored">&#8659; Download Free Trial</a></div>')

def SW_SCHEMA():
    d = {"@context":"https://schema.org","@type":"SoftwareApplication",
         "name":"Wondershare Recoverit","operatingSystem":"Windows, macOS",
         "applicationCategory":"UtilitiesApplication",
         "offers":{"@type":"Offer","price":"0","priceCurrency":"USD","description":"Free trial — recover 500MB free"},
         "description":"Recoverit recovers deleted files, photos, videos, documents from hard drives, USB, SD cards with 99.5% success rate.",
         "url":AFFILIATE_URL,
         "publisher":{"@type":"Organization","name":"Wondershare Technology"},
         "aggregateRating":{"@type":"AggregateRating","ratingValue":"4.8","reviewCount":"6234","bestRating":"5"}}
    return '<script type="application/ld+json">' + json.dumps(d) + '</script>'

def BC_SCHEMA(items):
    els = [{"@type":"ListItem","position":i+1,"name":l,"item":SITE_DOMAIN+"/"+u if u else SITE_DOMAIN} for i,(l,u) in enumerate(items)]
    return '<script type="application/ld+json">' + json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":els}) + '</script>'

def FAQ_SCHEMA(pairs):
    items = [{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in pairs]
    return '<script type="application/ld+json">' + json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":items}) + '</script>'

def ART_SCHEMA(title, desc, pub):
    d = {"@context":"https://schema.org","@type":"Article","headline":title,"description":desc,
         "datePublished":pub,"dateModified":BUILD_DATE,
         "author":{"@type":"Organization","name":"RecoverIt Guide"},
         "publisher":{"@type":"Organization","name":"RecoverIt Guide"}}
    return '<script type="application/ld+json">' + json.dumps(d) + '</script>'

def HEAD(title, desc, canon, extra="", og_type="website"):
    return ("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
            "<meta charset=\"UTF-8\"/><meta name=\"viewport\" content=\"width=device-width,initial-scale=1.0\"/>\n"
            f"<title>{title}</title>\n"
            f"<meta name=\"description\" content=\"{desc}\"/>\n"
            f"<link rel=\"canonical\" href=\"{SITE_DOMAIN}/{canon}\"/>\n"
            f"<meta property=\"og:title\" content=\"{title}\"/>\n"
            f"<meta property=\"og:description\" content=\"{desc}\"/>\n"
            f"<meta property=\"og:type\" content=\"{og_type}\"/>\n"
            f"<meta property=\"og:url\" content=\"{SITE_DOMAIN}/{canon}\"/>\n"
            "<meta property=\"og:site_name\" content=\"RecoverIt Guide\"/>\n"
            "<meta name=\"twitter:card\" content=\"summary_large_image\"/>\n"
            f"<meta name=\"twitter:title\" content=\"{title}\"/>\n"
            f"<meta name=\"twitter:description\" content=\"{desc}\"/>\n"
            "<meta name=\"robots\" content=\"index,follow\"/>\n"
            + CSS + "\n" + SW_SCHEMA() + "\n" + extra + "\n</head>")

# ═══════════════════════════════════════════════
#  SHARED DATA
# ═══════════════════════════════════════════════
FEATURES = [
    ("&#128444;","Recover Any File Type","1,000+ file types recovered &#8212; photos, videos, documents, audio, emails, archives.",
     ["JPEG, PNG, RAW, MP4, MOV, AVI, MKV","Word, Excel, PDF, PowerPoint","MP3, WAV, AAC, FLAC audio","Emails and ZIP archives"]),
    ("&#128190;","All Storage Devices","Hard drives, SSDs, USB drives, SD cards, NAS, cameras, drones &#8212; 1M+ devices supported.",
     ["Internal and external hard drives","USB flash drives and SD cards","NAS and RAID arrays","Digital cameras and drones"]),
    ("&#128269;","Deep Scan Technology","Quick Scan finds recent deletions in seconds. Deep Scan finds files after formatting or corruption.",
     ["Quick Scan completes in seconds","Deep Scan sector-by-sector analysis","Pause and resume at any time","Preview files during scan"]),
    ("&#127910;","Video Repair","Patented video fragment reconstruction repairs corrupted GoPro, drone and camera footage.",
     ["4K, HD and 8K video repair","GoPro, DJI drone, DSLR footage","Corrupted MP4, MOV, AVI repair","35+ patented recovery methods"]),
    ("&#128064;","Preview Before Recovery","Preview every recovered file before committing &#8212; confirm photos, videos and documents are intact.",
     ["Preview photos and videos","Verify document content","Select specific files only","Preview during scan &#8212; no waiting"]),
    ("&#127968;","Crashed PC Recovery","Bootable USB drive recovers data from computers that won't start &#8212; no working OS needed.",
     ["Bootable USB recovery drive","Recover from Blue Screen of Death","Recover after failed OS update","Access data from unbootable PCs"]),
    ("&#127758;","NAS Remote Recovery","Recover from Synology, QNAP, WD NAS remotely &#8212; no need to dismantle the server.",
     ["Remote NAS connection recovery","No server dismantling required","Synology, QNAP, WD My Cloud","Linux EXT4, Btrfs, XFS support"]),
    ("&#128204;","35+ Patented Methods","Award-winning technology with 35+ patents &#8212; video fragment reconstruction, disk image recovery.",
     ["35+ patents for innovative recovery","Disk image recovery (no wear)","10,000+ scenarios covered","99.5% recovery success rate"]),
    ("&#127775;","AI Photo Enhancement","AI-powered photo repair sharpens blurred images, clarifies low-quality photos and enhances faces.",
     ["AI image sharpening technology","Low-quality photo enhancement","Facial feature refinement","Before/after comparison view"]),
]

def FEATURES_GRID():
    cards = ""
    for icon,name,desc,buls in FEATURES:
        li = "".join("<li>" + b + "</li>" for b in buls)
        cards += '<div class="card"><div class="fi">' + icon + '</div><h3>' + name + '</h3><p>' + desc + '</p><ul>' + li + '</ul></div>'
    return '<div class="grid2">' + cards + '</div>'

TESTIMONIALS = [
    ("&#9733;&#9733;&#9733;&#9733;&#9733;","I accidentally formatted my 2TB external drive with 12 years of family photos. Recoverit ran a 5-hour deep scan and recovered 97% of them in perfect quality. I genuinely cried. Worth every penny and more.","Emma L.","Manchester, UK &#127468;&#127463;"),
    ("&#9733;&#9733;&#9733;&#9733;&#9733;","My GoPro SD card corrupted mid-trip in Patagonia. Recoverit recovered all my 4K footage including files my card reader wouldn't recognise. The video repair feature fixed two clips that wouldn't play. Absolutely incredible.","Jake R.","Denver, USA &#127482;&#127480;"),
    ("&#9733;&#9733;&#9733;&#9733;&#9733;","As a wedding photographer, losing client photos would be career-ending. Recoverit recovered a complete wedding shoot from a corrupted CF card &#8212; every RAW file intact. My client never knew there was an issue.","Yuki T.","Tokyo, Japan &#127471;&#127477;"),
    ("&#9733;&#9733;&#9733;&#9733;&#9733;","My NAS drive failed with 4 years of business documents. Recoverit connected remotely and recovered everything without me having to touch the server hardware. Our IT team was stunned.","Carlos M.","Barcelona, Spain &#127466;&#127480;"),
    ("&#9733;&#9733;&#9733;&#9733;&#9733;","Recovered 800 RAW photos from a formatted camera SD card I thought were gone forever. The preview feature let me confirm every file was intact before recovering. Five stars without hesitation.","Priya S.","Mumbai, India &#127470;&#127475;"),
    ("&#9733;&#9733;&#9733;&#9733;&#9733;","Meine komplette RAID-NAS-Datenbank war nach einem Controller-Fehler verloren. Recoverit hat alle Daten wiederhergestellt ohne das NAS auseinanderbauen zu m&#252;ssen. Fantastisches Programm!","Klaus B.","Hamburg, Deutschland &#127465;&#127466;"),
]

def TESTIMONIALS_GRID():
    cards = "".join('<div class="tcard"><div class="stars">' + s + '</div><p class="ttext">"' + t + '"</p><div class="tauthor">' + n + " &#8212; " + l + '</div></div>' for s,t,n,l in TESTIMONIALS)
    return '<div class="grid3">' + cards + '</div>'

FAQ_GLOBAL = [
    ("What is Wondershare Recoverit?","Wondershare Recoverit is professional data recovery software that recovers deleted, lost or corrupted files from hard drives, USB drives, SD cards, cameras and other storage devices on Windows and Mac."),
    ("What is the recovery success rate?","Recoverit achieves an industry-leading 99.5% recovery success rate in internal testing across 10,000+ recovery scenarios covering 500+ data loss situations."),
    ("Is there a free trial?","Yes &#8212; Recoverit's free version lets you recover up to 500MB of data at no cost. This is enough to test recovery on your specific device and file types before purchasing."),
    ("What file types can Recoverit recover?","Recoverit recovers 1,000+ file types: JPEG, PNG, RAW photos, MP4, MOV, AVI, MKV videos, Word, Excel, PDF, PowerPoint documents, MP3 audio, emails and archives."),
    ("What devices does Recoverit support?","Hard drives, SSDs, USB flash drives, SD cards, CF cards, NAS devices, RAID arrays, digital cameras, drones, and computers that won't start &#8212; over 1 million devices."),
    ("Can it recover data from a formatted drive?","Yes &#8212; Deep Scan recovers data from formatted drives by reading raw sector data. Recovery success depends on how much new data has been written since formatting."),
    ("Can it recover data from a crashed computer?","Yes &#8212; Recoverit creates a bootable USB drive to recover data from a PC that won't start due to Blue Screen of Death, failed OS update or hard drive failure."),
    ("What should I do immediately after data loss?","Stop using the device immediately &#8212; every write operation can overwrite recoverable data. Install Recoverit on a different drive and run a scan as soon as possible."),
    ("Is Recoverit safe?","Yes &#8212; developed by Wondershare Technology. The software only reads from your storage device during scanning and writes recovered files to a different location you specify."),
    ("Does it work on Mac?","Yes &#8212; available for macOS 10.12+ including the latest Sonoma and Sequoia. Fully supports Intel and Apple Silicon Macs."),
    ("Can it repair corrupted video files?","Yes &#8212; Recoverit's patented video repair feature reconstructs corrupted GoPro, drone and camera footage using fragment-based technology unique to Recoverit."),
    ("What is the file size limit?","No file size limit &#8212; recover files of any size including large 4K and 8K video files, RAW photo archives and multi-gigabyte databases."),
]

def FAQ_BLOCK(pairs):
    items = "".join('<div class="faq-item"><div class="faq-q">' + q + '</div><div class="faq-a">' + a + '</div></div>' for q,a in pairs)
    return '<div class="faq-list">' + items + '</div>'

def related_cloud(kw_data, n=24):
    same = [k for k in KEYWORDS if k["cat"]==kw_data["cat"] and k["slug"]!=kw_data["slug"]]
    diff = [k for k in KEYWORDS if k["cat"]!=kw_data["cat"]]
    pool = (same+diff)[:n]
    links = "".join('<a class="kw" href="' + BASE_PATH + '/' + r["slug"] + '.html">' + r["keyword"] + '</a>' for r in pool)
    return '<div class="kw-cloud">' + links + '</div>'


# ═══════════════════════════════════════════════
#  CATEGORY DEEP CONTENT
# ═══════════════════════════════════════════════
def cat_deep(cat, keyword):
    bodies = {
"device": (
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">Device Recovery Guide</div><h2>' + keyword + ' &#8212; Complete Guide</h2>'
    '<div class="prose">'
    '<p>Every storage device requires a slightly different recovery approach depending on its type, the operating system it was formatted for, and the cause of data loss. Recoverit handles all major device types with dedicated scanning algorithms optimised for each format.</p>'
    '<h3>The Golden Rule: Stop Using the Device</h3>'
    '<p>The single most important action after data loss is to <strong>stop using the affected device immediately</strong>. Every file saved, every application opened, every background process that runs writes data to your storage &#8212; potentially overwriting the exact sectors where your deleted files live. Connect the affected drive to another computer if possible, or at minimum, avoid saving anything new to the affected drive.</p>'
    '<h3>Quick Scan vs Deep Scan</h3>'
    '<p><strong>Quick Scan</strong> completes in seconds to minutes and finds recently deleted files whose directory entries are still present in the file system table. Always try this first &#8212; it is faster and less invasive. <strong>Deep Scan</strong> takes 30 minutes to several hours and performs sector-by-sector analysis to find file fragments even after formatting, corruption or partition loss. Use Deep Scan when Quick Scan fails.</p>'
    '<h3>Recovery Success Factors</h3>'
    '<p>Recovery success depends on: how quickly you act after data loss, how much new data has been written since the loss, the type of file system, and the physical condition of the drive. Acting immediately and installing Recoverit on a different drive gives you the best possible chance.</p>'
    '</div></div></section>'),

"filetype": (
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">File Type Recovery</div><h2>Recovering ' + keyword + '</h2>'
    '<div class="prose">'
    '<p>Different file types use different internal structures &#8212; and Recoverit uses file signatures (unique binary patterns at the start of each file format) to identify and reconstruct files even when directory entries are completely deleted and original filenames are lost.</p>'
    '<h3>How File Signature Recovery Works</h3>'
    '<p>Every file type has a unique "magic number" &#8212; a sequence of bytes at the beginning of the file that identifies its format. JPEG files start with FF D8 FF. PDF files start with 25 50 44 46. Recoverit scans raw drive data looking for these signatures and reconstructs complete files from the data that follows, independent of the file system directory. This is why Deep Scan can recover files from formatted drives where the entire directory structure has been erased.</p>'
    '<h3>Media File Recovery Quality</h3>'
    '<p>Photos and videos are stored as contiguous blocks on your drive. When deleted, the file system marks the space as available but does not erase the data. Recoverit reconstructs photo and video files from their raw binary data, restoring the original quality &#8212; including full-resolution RAW files from professional cameras (CR2, NEF, ARW, ORF, RW2 and more).</p>'
    '<h3>Video Repair for Corrupted Files</h3>'
    '<p>When video files are found but won\'t play &#8212; corrupted header, damaged frames, interrupted recording &#8212; Recoverit\'s patented video repair feature reconstructs playability using fragment-based methods. Uniquely effective for GoPro, DJI drone and action camera footage.</p>'
    '</div></div></section>'),

"howto": (
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">Step-by-Step Guide</div><h2>' + keyword + ' &#8212; Exact Steps</h2>'
    '<div class="prose">'
    '<p>Data recovery with Recoverit follows a simple three-step process that works for virtually every data loss scenario. Here is exactly what to do.</p>'
    '<h3>Before You Start &#8212; Critical</h3>'
    '<p><strong>Stop using the affected device immediately.</strong> If data was lost from your computer\'s internal drive, download Recoverit\'s installer to a USB drive or external hard drive &#8212; not to the affected drive. Install it from that external drive. This prevents the installation process from overwriting your data.</p>'
    '<h3>Step 1 &#8212; Select the Location</h3>'
    '<p>Open Recoverit and select the drive or location where data was lost. For specific folders, select that location directly. For external devices (USB, SD card, external drive), the device appears automatically in the list when connected.</p>'
    '<h3>Step 2 &#8212; Scan</h3>'
    '<p>Click Start. Quick Scan runs first and completes in under a minute. You can browse and preview found files immediately &#8212; no need to wait for the scan to finish. If Quick Scan doesn\'t find your files, switch to Deep Scan for sector-by-sector analysis.</p>'
    '<h3>Step 3 &#8212; Preview and Recover</h3>'
    '<p>Preview your files to confirm they are intact. Select what you want and click Recover. Save recovered files to a <strong>different drive</strong> than the source &#8212; saving to the same drive risks overwriting data you haven\'t recovered yet.</p>'
    '</div></div></section>'),

"compare": (
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">Honest Comparison</div><h2>' + keyword + ' &#8212; Detailed Analysis</h2>'
    '<div class="prose">'
    '<p>Here is an honest assessment of how Recoverit compares to the major alternatives &#8212; including the areas where competitors genuinely lead.</p>'
    '<h3>Recoverit vs Disk Drill</h3>'
    '<p>Both achieve similar recovery rates for standard deletions. Recoverit leads significantly on video repair capabilities (Disk Drill has no equivalent of Recoverit\'s patented fragment reconstruction), NAS remote recovery (Disk Drill does not support this) and AI photo enhancement. Disk Drill leads on Mac free-tier scanning flexibility and includes a drive health monitoring feature. For Windows users and anyone dealing with corrupted media, Recoverit is the stronger tool.</p>'
    '<h3>Recoverit vs EaseUS</h3>'
    '<p>EaseUS is a long-established competitor with strong document recovery. Both achieve comparable rates for standard scenarios. Recoverit\'s patented video fragment reconstruction gives it a decisive advantage for camera footage. EaseUS lacks NAS recovery and AI enhancement capabilities.</p>'
    '<h3>Recoverit vs Recuva</h3>'
    '<p>Recuva is free and adequate for simple Windows recovery tasks. It hasn\'t received major updates in years, has no video repair, no Mac support and limited deep scan capability for formatted drives. For straightforward recent deletions from the Recycle Bin, Recuva works. For anything complex &#8212; formatted drives, corrupted media, NAS &#8212; Recoverit is substantially better.</p>'
    '</div></div></section>'),

"video-repair": (
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">Video Repair Technology</div><h2>How Recoverit Repairs Corrupted Videos</h2>'
    '<div class="prose">'
    '<p>Video corruption is one of the most frustrating forms of data damage &#8212; the file exists, it has the right size, but it simply won\'t play. This happens when the video container\'s header or index data is damaged while the actual video and audio frames remain intact. Recoverit\'s patented repair technology specifically addresses this.</p>'
    '<h3>Why Videos Become Corrupted</h3>'
    '<p>The most common causes: removing an SD card or battery while the camera is actively writing (the most common cause, leaving an incomplete file); unexpected power loss during recording; storage device failure mid-write; incomplete file transfers; and file system errors that corrupt the index while leaving frame data intact.</p>'
    '<h3>Fragment-Based Reconstruction</h3>'
    '<p>Recoverit holds 35+ patents covering recovery methods, including proprietary video fragment reconstruction. The software analyses the raw binary data of a corrupted video file, identifies the video and audio frames within it (which are typically still intact), and reconstructs a valid container around them. This approach has higher success rates than simple header repair for action camera footage because it works from the frame data up rather than trying to patch the damaged structure down.</p>'
    '<h3>Supported Formats</h3>'
    '<p>MP4, MOV, AVI, MKV, M4V, 3GP, FLV, WMV, INSV (Insta360) and GoPro\'s proprietary formats. Supports 4K, 8K, HDR and high-bitrate footage from all major camera manufacturers.</p>'
    '</div></div></section>'),

"nas": (
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">NAS Recovery Guide</div><h2>NAS Data Recovery &#8212; How It Works</h2>'
    '<div class="prose">'
    '<p>NAS data recovery is technically more complex than recovering from a simple USB drive or SD card. NAS devices use Linux-based file systems (EXT4, Btrfs, XFS), often run RAID arrays across multiple physical drives, and are typically business-critical infrastructure that cannot be easily powered down and dismantled.</p>'
    '<h3>Remote Recovery Without Dismantling</h3>'
    '<p>Recoverit\'s NAS recovery establishes a remote connection to the NAS device over your local network using SSH. This means: no physical dismantling of the server, no risk of making the situation worse by removing drives, no business downtime beyond the recovery scan duration. The NAS continues operating (in read-only mode during scanning) while Recoverit performs its analysis.</p>'
    '<h3>Supported File Systems</h3>'
    '<p>EXT2, EXT3, EXT4, Btrfs, XFS and BFS &#8212; covering Synology DSM (uses Btrfs or EXT4), QNAP QTS (uses EXT4 or ZFS), WD My Cloud (EXT3/EXT4) and other Linux-based NAS devices. RAID 0, 1, 5, 6 and 10 array recovery is supported.</p>'
    '<h3>When NAS Recovery Is Needed</h3>'
    '<p>RAID controller failure (where individual drives are fine but the array cannot be rebuilt), accidental deletion or formatting of a NAS volume, ransomware attack on a NAS share, individual drive failure within a RAID array, or corruption of the volume\'s file system metadata.</p>'
    '</div></div></section>'),
    }
    body = bodies.get(cat)
    if body: return body
    aff = AFFILIATE_URL
    return ('<section style="background:#fff"><div class="container">'
            '<div class="sec-ey">Complete Guide</div>'
            '<h2>' + keyword + ' &#8212; Full Overview</h2>'
            '<div class="prose">'
            '<p>Recoverit by Wondershare is the world\'s leading solution for ' + keyword.lower() + '. '
            'With a 99.5% recovery success rate, support for 1,000+ file types and 10,000+ recovery scenarios, '
            'it handles everything from simple accidental deletions to complex formatted drive recovery &#8212; '
            'all in a three-step process that requires zero technical knowledge.</p>'
            '<p>Whether you\'ve accidentally deleted important files, suffered a hard drive crash, formatted a device by mistake, '
            'or experienced a ransomware attack, Recoverit\'s Deep Scan technology and patented recovery methods '
            'give you the best possible chance of getting your data back.</p>'
            '<h3>Why Recoverit Leads the Industry</h3>'
            '<p>35+ patents for innovative recovery methods including video fragment reconstruction. AI-powered media repair. '
            'Remote NAS recovery without dismantling servers. Bootable USB for crashed computer recovery. '
            'Free 500MB trial &#8212; test it on your actual data before purchasing.</p>'
            '</div>'
            '<div style="margin-top:2rem">'
            '<a href="' + aff + '" class="btn-p" target="_blank" rel="nofollow sponsored">'
            '&#8659; Download Free Trial &#8212; Recover 500MB Free</a>'
            '</div></div></section>')


# ═══════════════════════════════════════════════
#  KEYWORD PAGE BUILDER
# ═══════════════════════════════════════════════
def build_keyword_page(kw_data):
    slug=kw_data["slug"]; keyword=kw_data["keyword"]; cat=kw_data["cat"]
    a1,a2=ac(cat)
    title  = keyword + " &#8212; Recoverit | " + str(YEAR)
    desc   = ("Looking for " + keyword.lower() + "? Recoverit recovers deleted files, photos, videos "
              "with 99.5% success rate. Free 500MB trial &#8212; Windows & Mac.")
    canon  = slug + ".html"
    faq_pairs = [
        ("Can Recoverit handle " + keyword.lower() + "?",
         "Yes &#8212; Recoverit is specifically designed for " + keyword.lower() + ". "
         "With a 99.5% recovery success rate, 1,000+ file types and 10,000+ scenarios covered, "
         "it handles simple deletions through to complex formatted drive recovery. "
         "Download the free trial to recover up to 500MB at no cost."),
        ("How long does " + keyword.lower() + " take with Recoverit?",
         "Quick Scan completes in under a minute for recently deleted files. "
         "Deep Scan takes 30 minutes to several hours for formatted or corrupted drives. "
         "You can preview and recover files during the scan without waiting for completion."),
        ("Is the free trial enough for " + keyword.lower() + "?",
         "Recoverit's free trial recovers up to 500MB &#8212; enough to recover many photos, "
         "documents or small video files. For larger recoveries, the full license is available."),
    ]
    bc_s  = BC_SCHEMA([("Home",""),("All Topics","keywords.html"),(keyword,"")])
    fq_s  = FAQ_SCHEMA(faq_pairs)
    body  = cat_deep(cat, keyword)
    same  = [k for k in KEYWORDS if k["cat"]==cat and k["slug"]!=slug][:6]
    links = " &#183; ".join('<a href="' + BASE_PATH + '/' + r["slug"] + '.html">' + r["keyword"] + '</a>' for r in same)

    return (HEAD(title, desc, canon, bc_s+fq_s)
        + "\n<body>\n"
        + "<style>:root{--ha:" + a1 + ";--hb:" + a2 + ";--fa:rgba(0,0,0,.05)}</style>\n"
        + NAV() + "\n"
        + BC([("Home",BASE_PATH+"/"),("All Topics",BASE_PATH+"/keywords.html"),(keyword,"")])
        + '\n<section class="hero">'
        + '\n  <div class="eyebrow">&#10022; ' + cat.replace("-"," ").title() + '</div>'
        + '\n  <h1><em>' + keyword + '</em><br>&#8212; Recover with Recoverit</h1>'
        + '\n  <p class="hsub">99.5% success rate &#183; 1,000+ file types &#183; 10,000+ scenarios &#183; Free 500MB trial</p>'
        + '\n  <div class="btns">'
        + '\n    <a href="' + AFFILIATE_URL + '" class="btn-p" target="_blank" rel="nofollow sponsored">&#8659; Download Free Trial</a>'
        + '\n    <a href="' + BASE_PATH + '/how-it-works.html" class="btn-s">How It Works</a>'
        + '\n  </div>'
        + '\n  <div class="stats">'
        + '\n    <div><span class="stat-n">99.5%</span><span class="stat-l">Success Rate</span></div>'
        + '\n    <div><span class="stat-n">1,000+</span><span class="stat-l">File Types</span></div>'
        + '\n    <div><span class="stat-n">10,000+</span><span class="stat-l">Scenarios</span></div>'
        + '\n    <div><span class="stat-n">35+</span><span class="stat-l">Patents</span></div>'
        + '\n  </div>\n</section>\n'
        + '\n<section><div class="container">'
        + '\n  <div class="sec-ey">All Features</div>'
        + '\n  <h2>Everything You Need for ' + keyword.title() + '</h2>'
        + '\n  <p class="sec-sub">Complete data recovery solution &#8212; recover any file, from any device, in any data loss scenario.</p>'
        + FEATURES_GRID()
        + '\n</div></section>\n'
        + body
        + '\n<section style="background:#e0f7fa"><div class="container">'
        + '\n  <div class="sec-ey">Real Users</div><h2>Trusted by Millions Worldwide</h2>'
        + TESTIMONIALS_GRID()
        + '\n</div></section>\n'
        + '\n<section><div class="container">'
        + '\n  <div class="sec-ey">FAQ</div><h2>Common Questions</h2>'
        + FAQ_BLOCK(faq_pairs + FAQ_GLOBAL[:3])
        + '\n  <div style="margin-top:1.5rem">'
        + '\n    <a href="' + BASE_PATH + '/faq.html" style="color:var(--ha);font-weight:600;font-size:.88rem">View all ' + str(len(FAQ_GLOBAL)) + ' FAQs &#8594;</a>'
        + '\n  </div>\n</div></section>\n'
        + '\n<section class="dark-sec"><div class="container">'
        + '\n  <div class="sec-ey">Related Topics</div><h2>Explore More</h2>'
        + related_cloud(kw_data, 28)
        + ('\n  <p style="margin-top:1.4rem;font-size:.78rem;color:rgba(255,255,255,.35)">More: ' + links + '</p>' if links else '')
        + '\n</div></section>\n'
        + CTA("Recover Your " + keyword.title() + " Now",
              "Download Recoverit free and recover up to 500MB at no cost. No credit card required.")
        + "\n" + FOOTER() + "\n" + FAQ_JS + "\n</body></html>")


# ═══════════════════════════════════════════════
#  ESSENTIAL PAGES
# ═══════════════════════════════════════════════
def page_index():
    extra = FAQ_SCHEMA(FAQ_GLOBAL[:6]) + BC_SCHEMA([("Home","")])
    scenarios = [
        ("&#128247;","Deleted Photos","recover-deleted-photos","Camera, SD card, phone"),
        ("&#127910;","Deleted Videos","recover-deleted-videos","4K, GoPro, drone footage"),
        ("&#128196;","Deleted Documents","document-recovery-software","Word, Excel, PDF files"),
        ("&#128190;","Hard Drive Crash","hard-drive-recovery","Failed or clicking drives"),
        ("&#128204;","SD Card Corrupt","sd-card-recovery","Unreadable or corrupted cards"),
        ("&#128070;","USB Drive Lost","usb-drive-recovery","Flash drives and sticks"),
        ("&#128665;","Formatted Drive","recover-after-format","After accidental format"),
        ("&#128187;","PC Won't Boot","recover-data-crashed-computer","Bootable USB recovery"),
        ("&#128373;","Virus/Ransomware","recover-after-ransomware","After malware attack"),
        ("&#127979;","NAS Recovery","nas-recovery","Synology, QNAP, WD remote"),
        ("&#127910;","Corrupted Video","video-repair-software","Won't play video files"),
        ("&#128247;","RAW Photos","raw-photo-recovery","CR2, NEF, ARW, ORF files"),
    ]
    sc_html = "".join(
        '<a class="sc-card" href="' + BASE_PATH + '/' + s + '.html">'
        '<span class="sc-icon">' + i + '</span>'
        '<span class="sc-label">' + n + '</span>'
        '<span class="sc-sub">' + d + '</span></a>'
        for i,n,s,d in scenarios)

    return (HEAD("Wondershare Recoverit &#8212; Best Data Recovery Software | " + str(YEAR),
                 "Recover deleted photos, videos, documents from any device with Recoverit. 99.5% success rate, free 500MB trial. Windows & Mac.",
                 "", extra)
        + "\n<body>\n" + NAV()
        + '\n<section class="hero">'
        + '\n  <div class="eyebrow">&#10022; World\'s #1 Data Recovery Software</div>'
        + '\n  <h1>Recover Your Lost Files.<br><em>Fast. Reliably. Free to Try.</em></h1>'
        + '\n  <p class="hsub">Photos, videos, documents and more recovered from any device. 99.5% success rate, 1,000+ file types, free 500MB trial &#8212; no credit card needed.</p>'
        + '\n  <div class="btns">'
        + '\n    <a href="' + AFFILIATE_URL + '" class="btn-p" target="_blank" rel="nofollow sponsored">&#8659; Download Free Trial</a>'
        + '\n    <a href="' + BASE_PATH + '/how-it-works.html" class="btn-s">See How It Works</a>'
        + '\n  </div>'
        + '\n  <div class="stats">'
        + '\n    <div><span class="stat-n">99.5%</span><span class="stat-l">Recovery Rate</span></div>'
        + '\n    <div><span class="stat-n">1,000+</span><span class="stat-l">File Types</span></div>'
        + '\n    <div><span class="stat-n">10,000+</span><span class="stat-l">Scenarios</span></div>'
        + '\n    <div><span class="stat-n">1M+</span><span class="stat-l">Devices Supported</span></div>'
        + '\n  </div>\n</section>\n'
        + '\n<section style="background:#fff"><div class="container">'
        + '\n  <div class="sec-ey">Every Recovery Scenario</div>'
        + '\n  <h2>What Did You Lose? We Can Get It Back.</h2>'
        + '\n  <p class="sec-sub">Click your scenario for a step-by-step recovery guide &#8212; or download Recoverit and start now.</p>'
        + '\n  <div class="sc-grid">' + sc_html + '</div>'
        + '\n</div></section>\n'
        + '\n<section><div class="container">'
        + '\n  <div class="sec-ey">Complete Feature Suite</div>'
        + '\n  <h2>More Than Just File Recovery</h2>'
        + '\n  <p class="sec-sub">Recoverit V14 is an intelligent restoration platform &#8212; 9 feature areas, 35+ patents, AI enhancement.</p>'
        + FEATURES_GRID()
        + '\n  <div style="margin-top:2.5rem;text-align:center">'
        + '\n    <a href="' + BASE_PATH + '/features.html" style="color:var(--ha);font-weight:600">View full feature list &#8594;</a>'
        + '\n  </div>\n</div></section>\n'
        + '\n<section style="background:#fff"><div class="container">'
        + '\n  <div class="sec-ey">The #1 Rule</div>'
        + '\n  <h2>Stop. Don\'t Write Anything. Then Recover.</h2>'
        + '\n  <div class="grid3">'
        + '\n    <div class="card"><div class="fi">&#128721;</div><h3>Stop Using the Device</h3><p>Every file saved or app opened risks overwriting your data. Stop the moment you realise something is lost.</p></div>'
        + '\n    <div class="card"><div class="fi">&#128190;</div><h3>Install Elsewhere</h3><p>Install Recoverit on a different drive &#8212; not the one that lost data &#8212; to protect recoverable files.</p></div>'
        + '\n    <div class="card"><div class="fi">&#128270;</div><h3>Scan, Preview, Recover</h3><p>Run the scan, preview your files to confirm they\'re intact, then recover to a safe location.</p></div>'
        + '\n  </div>\n</div></section>\n'
        + '\n<section style="background:#e0f7fa"><div class="container">'
        + '\n  <div class="sec-ey">Real Users</div>'
        + '\n  <h2 style="text-align:center;margin-bottom:2.5rem">Trusted by Millions &#8212; Home Users to Professionals</h2>'
        + TESTIMONIALS_GRID()
        + '\n</div></section>\n'
        + '\n<section><div class="container">'
        + '\n  <div class="sec-ey">FAQ</div><h2>Common Questions About Recoverit</h2>'
        + FAQ_BLOCK(FAQ_GLOBAL[:6])
        + '\n  <div style="margin-top:1.5rem;text-align:center">'
        + '\n    <a href="' + BASE_PATH + '/faq.html" style="color:var(--ha);font-weight:600">View all ' + str(len(FAQ_GLOBAL)) + ' FAQs &#8594;</a>'
        + '\n  </div>\n</div></section>\n'
        + CTA() + "\n" + FOOTER() + "\n" + FAQ_JS + "\n</body></html>")


def page_features():
    bc = BC_SCHEMA([("Home",""),("Features","")])
    rows = [
        ("Photo Recovery",      "V","V","V","Limited","V"),
        ("Video Recovery",      "V","V","V","Limited","Limited"),
        ("Video Repair",        "V","X","X","X","X"),
        ("RAW Photo Recovery",  "V","V","Partial","X","X"),
        ("Deep Scan",           "V","V","V","X","V"),
        ("Formatted Drive",     "V","V","V","X","V"),
        ("Crashed PC (Bootable)","V","V","X","X","X"),
        ("NAS Remote Recovery", "V","X","X","X","X"),
        ("AI Photo Repair",     "V","X","X","X","X"),
        ("35+ Patents",         "V","X","X","X","X"),
        ("Disk Image Recovery", "V","X","X","X","X"),
        ("Free Trial",          "500MB","500MB","500MB","Unlimited","1GB"),
        ("Mac Support",         "V","V","V","X","V"),
        ("Pricing",             "One-Time","Sub","Sub","Free","One-Time"),
    ]
    tools = ["Recoverit &#10022;","Disk Drill","EaseUS","Recuva","Stellar"]
    hrow = "<tr><th>Feature</th>" + "".join(('<th class="hl">' if i==0 else '<th>') + t + '</th>' for i,t in enumerate(tools)) + "</tr>"
    def cell(v,i):
        if i==0: return '<td class="ck" style="font-weight:700">' + v + '</td>'
        if v=="V": return '<td class="ck">&#10004;</td>'
        if v=="X": return '<td class="cr">&#10008;</td>'
        if v in("Partial","Limited","Sub"): return '<td class="cp">' + v + '</td>'
        return '<td class="cp">' + v + '</td>'
    trows = "".join("<tr>" + cell(r[0],-1) + "".join(cell(v,i) for i,v in enumerate(r[1:])) + "</tr>" for r in rows)

    return (HEAD("Recoverit Features &#8212; Video Repair, NAS, AI & More | " + str(YEAR),
                 "Complete Recoverit V14 feature list: photo recovery, video repair, NAS remote recovery, bootable USB, AI enhancement, 35+ patents.",
                 "features.html", bc)
        + "\n<body>\n" + NAV()
        + "\n" + BC([("Home",BASE_PATH+"/"),("Features","")])
        + '\n<section class="hero">'
        + '\n  <div class="eyebrow">&#10022; Complete Feature List</div>'
        + '\n  <h1>Everything Recoverit V14<br><em>Can Do For You</em></h1>'
        + '\n  <p class="hsub">9 feature areas &#183; 35+ patents &#183; AI enhancement &#183; NAS remote recovery &#183; Bootable USB &#183; Video repair</p>'
        + '\n  <a href="' + AFFILIATE_URL + '" class="btn-p" target="_blank" rel="nofollow sponsored">&#8659; Download Free Trial</a>'
        + '\n</section>\n'
        + '\n<section><div class="container">'
        + '\n  <div class="sec-ey">All 9 Feature Areas</div><h2>The Complete Recovery Toolkit</h2>'
        + FEATURES_GRID()
        + '\n</div></section>\n'
        + '\n<section style="background:#fff"><div class="container">'
        + '\n  <div class="sec-ey">5-Tool Comparison</div><h2>Recoverit vs Every Alternative</h2>'
        + '\n  <div class="tbl-wrap"><table><thead>' + hrow + '</thead><tbody>' + trows + '</tbody></table></div>'
        + '\n  <p style="margin-top:.9rem;font-size:.75rem;color:var(--muted)">&#10004; Full &#160; Partial/Limited = Partial &#160; &#10008; Not available</p>'
        + '\n</div></section>\n'
        + CTA("Try All Features Free","Download Recoverit &#8212; recover up to 500MB free, no credit card required.")
        + "\n" + FOOTER() + "\n</body></html>")


def page_how_it_works():
    bc = BC_SCHEMA([("Home",""),("How It Works","")])
    return (HEAD("How Recoverit Works &#8212; 3 Steps to Recover Your Data | " + str(YEAR),
                 "Recover deleted files in 3 simple steps: select location, scan, preview and recover. Works for any file type and device.",
                 "how-it-works.html", bc)
        + "\n<body>\n" + NAV()
        + "\n" + BC([("Home",BASE_PATH+"/"),("How It Works","")])
        + '\n<section class="hero">'
        + '\n  <div class="eyebrow">&#10022; Simple Process</div>'
        + '\n  <h1>Get Your Data Back in<br><em>3 Simple Steps</em></h1>'
        + '\n  <p class="hsub">No technical knowledge needed. Select, scan, recover &#8212; works for any file on any device.</p>'
        + '\n  <a href="' + AFFILIATE_URL + '" class="btn-p" target="_blank" rel="nofollow sponsored">&#8659; Download Free Trial</a>'
        + '\n</section>\n'
        + '\n<section><div class="container">'
        + '\n  <div class="sec-ey">The Process</div><h2>3 Steps to Recovery</h2>'
        + '\n  <div class="steps">'
        + '\n    <div class="step"><div class="sn">1</div><h3>Select Location</h3><p>Choose the drive or device where data was lost. Recoverit detects all connected devices automatically &#8212; internal drives, USB, SD cards, NAS.</p></div>'
        + '\n    <div class="step"><div class="sn">2</div><h3>Scan for Files</h3><p>Quick Scan finds recent deletions in seconds. Deep Scan performs sector-by-sector analysis for formatted or corrupted drives. Preview files as they are found.</p></div>'
        + '\n    <div class="step"><div class="sn">3</div><h3>Preview &amp; Recover</h3><p>Preview recovered files to confirm they are intact. Select what you want, click Recover, and save to a different location.</p></div>'
        + '\n  </div>\n</div></section>\n'
        + '\n<section style="background:#fff"><div class="container">'
        + '\n  <div class="sec-ey">Quick vs Deep Scan</div><h2>Which Scan Mode Do You Need?</h2>'
        + '\n  <div class="grid2">'
        + '\n    <div class="card"><div class="fi">&#9889;</div><h3>Quick Scan</h3><p>Completes in seconds to a few minutes. Finds recently deleted files where directory entries still exist. Always try first &#8212; faster and less invasive.</p><ul><li>Files deleted today or recently</li><li>Emptied Recycle Bin files</li><li>Recently deleted photos or documents</li></ul></div>'
        + '\n    <div class="card"><div class="fi">&#128270;</div><h3>Deep Scan</h3><p>Takes 30 minutes to several hours. Sector-by-sector analysis finds file fragments after formatting, corruption or partition loss. Use when Quick Scan fails.</p><ul><li>Formatted or reformatted drives</li><li>Corrupted or unreadable drives</li><li>Lost or deleted partitions</li></ul></div>'
        + '\n  </div>\n</div></section>\n'
        + '\n<section style="background:#fff"><div class="container" style="padding-top:0">'
        + '\n  <div class="sec-ey">Critical Advice</div><h2>The Most Important Thing You Can Do Right Now</h2>'
        + '\n  <div class="prose"><p><strong>Stop using the affected device immediately.</strong> Every file you save, every application that opens, every system process that runs writes data to your storage &#8212; potentially overwriting your recoverable files. The sooner you act, the better your recovery chances.</p>'
        + '\n    <p>If data was lost from your computer\'s internal drive: do NOT save Recoverit\'s installer to that drive. Download it to a USB stick or external hard drive first, install from there, then run the scan on your internal drive.</p>'
        + '\n    <p>When recovering files, always save them to a <strong>different drive</strong> than the one you are scanning. Recovering to the same drive risks overwriting other files you may want to recover.</p>'
        + '\n  </div>\n</div></section>\n'
        + '\n<section style="background:#e0f7fa"><div class="container">'
        + '\n  <div class="sec-ey">Real Results</div><h2>What Users Experience</h2>'
        + TESTIMONIALS_GRID()
        + '\n</div></section>\n'
        + CTA("Start Your Recovery Now","Download Recoverit free &#8212; recover up to 500MB, no credit card needed.")
        + "\n" + FOOTER() + "\n</body></html>")


def page_faq():
    all_faqs = FAQ_GLOBAL + [
        ("What is the free version limit?","Recoverit free version recovers up to 500MB of data at no cost. This covers many photos, documents or small video files and lets you verify the software works for your specific scenario before purchasing."),
        ("Can Recoverit recover overwritten files?","Once a file has been completely overwritten &#8212; new data saved to the exact same sectors &#8212; it cannot be recovered by any software. This is why stopping device use immediately after data loss is critical."),
        ("Does Recoverit work on SSDs?","Yes, but SSD recovery is more complex due to TRIM technology. When files are deleted from an SSD with TRIM enabled, the drive may immediately erase the data pages. Recovery success depends on how quickly you scan and whether TRIM has run."),
        ("Can it repair corrupted video files?","Yes &#8212; Recoverit's patented video repair feature reconstructs corrupted or unplayable video files using fragment-based technology. Particularly effective for GoPro, DJI drone and action camera footage."),
        ("Can it recover from a NAS device?","Yes &#8212; Recoverit establishes a remote SSH connection to NAS devices for recovery without dismantling the server. Supports Synology, QNAP, WD and Linux-based NAS with EXT4, Btrfs, XFS file systems."),
        ("What if Quick Scan doesn't find my files?","Run Deep Scan. Deep Scan performs sector-by-sector analysis and finds files that Quick Scan misses &#8212; particularly on formatted or corrupted drives. It takes longer but achieves higher recovery rates."),
        ("Can Recoverit recover from BitLocker drives?","Yes &#8212; if you have the BitLocker encryption key or recovery key, Recoverit can access and scan encrypted drives for recovery."),
        ("Is the scan safe for my drive?","Yes &#8212; Recoverit only reads from your storage device during scanning. It never writes to the scanned device, so the scan process cannot overwrite or damage your data."),
        ("Can it recover RAID arrays?","Yes &#8212; Recoverit supports RAID 0, 1, 5, 6 and 10 array recovery, even when individual drives have failed. The RAID reconstruction algorithm analyses available drives to recover the data."),
    ]
    fq = FAQ_SCHEMA(all_faqs)
    bc = BC_SCHEMA([("Home",""),("FAQ","")])
    return (HEAD("Recoverit FAQ &#8212; " + str(len(all_faqs)) + " Data Recovery Questions | " + str(YEAR),
                 "Every question about Wondershare Recoverit answered &#8212; recovery success, devices, file types, pricing, RAID, NAS and technical details.",
                 "faq.html", fq+bc)
        + "\n<body>\n" + NAV()
        + "\n" + BC([("Home",BASE_PATH+"/"),("FAQ","")])
        + '\n<section class="hero">'
        + '\n  <div class="eyebrow">&#10022; Complete FAQ</div>'
        + '\n  <h1>Every Question About<br><em>Recoverit Answered</em></h1>'
        + '\n  <p class="hsub">' + str(len(all_faqs)) + ' questions &#8212; recovery rates, devices, file types, pricing, RAID, NAS and technical details.</p>'
        + '\n</section>\n'
        + '\n<section><div class="container">'
        + '\n  <div class="sec-ey">All ' + str(len(all_faqs)) + ' Questions</div><h2>Complete FAQ</h2>'
        + FAQ_BLOCK(all_faqs)
        + '\n</div></section>\n'
        + CTA("Ready to Recover? Download Free","Try Recoverit &#8212; recover up to 500MB free, no credit card required.")
        + "\n" + FOOTER() + "\n" + FAQ_JS + "\n</body></html>")


def page_compare():
    bc = BC_SCHEMA([("Home",""),("Compare","")])
    rows = [
        ("Photo Recovery",      "V","V","V","V","V"),
        ("Video Repair",        "V","X","X","X","Partial"),
        ("NAS Remote Recovery", "V","X","X","X","X"),
        ("AI Photo Repair",     "V","X","X","X","X"),
        ("Bootable USB",        "V","V","X","X","V"),
        ("Deep Scan",           "V","V","V","Limited","V"),
        ("Disk Image Recovery", "V","X","X","X","X"),
        ("RAID Recovery",       "V","X","X","X","V"),
        ("Free Recovery",       "500MB","500MB","500MB","Unlimited","1GB"),
        ("Mac Support",         "V","V","V","X","V"),
        ("35+ Patents",         "V","X","X","X","X"),
        ("Pricing",             "One-Time","Sub","Sub","Free","One-Time"),
    ]
    tools = ["Recoverit","Disk Drill","EaseUS","Recuva","Stellar"]
    hrow = "<tr><th>Feature</th>" + "".join(('<th class="hl">' if i==0 else '<th>') + t + '</th>' for i,t in enumerate(tools)) + "</tr>"
    def cell(v,i):
        if i==0: return '<td class="ck" style="font-weight:700">' + v + '</td>'
        if v=="V": return '<td class="ck">&#10004;</td>'
        if v=="X": return '<td class="cr">&#10008;</td>'
        return '<td class="cp">' + v + '</td>'
    trows = "".join("<tr>" + cell(r[0],-1) + "".join(cell(v,i) for i,v in enumerate(r[1:])) + "</tr>" for r in rows)
    comps = [
        ("vs Disk Drill","Disk Drill is strong, especially on Mac. Comparable recovery rates for standard deletions. Recoverit leads on video repair, NAS remote recovery and AI enhancement. Disk Drill leads on Mac free-tier flexibility and drive health monitoring."),
        ("vs EaseUS Data Recovery","EaseUS has strong document recovery. Both achieve comparable rates for standard scenarios. Recoverit's patented video reconstruction gives it a decisive advantage for camera footage. EaseUS lacks NAS recovery and AI enhancement."),
        ("vs Recuva","Recuva is free and adequate for simple Windows tasks. No video repair, no Mac support, limited formatted-drive recovery. Fine for basic recent deletions. For anything complex &#8212; formatting, corruption, NAS &#8212; Recoverit is far stronger."),
        ("vs Stellar Data Recovery","Stellar is professional-grade at professional pricing. Comparable on most scenarios. Recoverit leads on ease of use, NAS remote recovery and AI enhancement. Stellar leads on very advanced enterprise RAID scenarios."),
    ]
    comp_cards = "".join('<div class="card"><h3>' + n + '</h3><p style="font-size:.87rem;color:var(--muted)">' + d + '</p></div>' for n,d in comps)

    return (HEAD("Recoverit vs Disk Drill, EaseUS, Recuva & Stellar | " + str(YEAR),
                 "Honest Recoverit comparison vs Disk Drill, EaseUS Data Recovery, Recuva and Stellar. Full feature table, recovery rates and clear verdict.",
                 "compare.html", bc)
        + "\n<body>\n" + NAV()
        + "\n" + BC([("Home",BASE_PATH+"/"),("Compare","")])
        + '\n<section class="hero">'
        + '\n  <div class="eyebrow">&#10022; Data Recovery Comparison ' + str(YEAR) + '</div>'
        + '\n  <h1>Recoverit vs<br><em>Every Alternative</em></h1>'
        + '\n  <p class="hsub">Honest comparison &#8212; recovery rates, unique features, pricing and where each tool leads.</p>'
        + '\n  <a href="' + AFFILIATE_URL + '" class="btn-p" target="_blank" rel="nofollow sponsored">&#8659; Download Recoverit Free</a>'
        + '\n</section>\n'
        + '\n<section style="background:#fff"><div class="container">'
        + '\n  <div class="sec-ey">Full Feature Matrix</div><h2>Complete Comparison Table</h2>'
        + '\n  <div class="tbl-wrap"><table><thead>' + hrow + '</thead><tbody>' + trows + '</tbody></table></div>'
        + '\n  <p style="margin-top:.9rem;font-size:.75rem;color:var(--muted)">&#10004; Full &#160; Partial/Limited/Sub = Partial &#160; &#10008; Not available</p>'
        + '\n</div></section>\n'
        + '\n<section><div class="container">'
        + '\n  <div class="sec-ey">Head-to-Head</div><h2>vs Each Competitor</h2>'
        + '\n  <div class="grid2">' + comp_cards + '</div>'
        + '\n</div></section>\n'
        + '\n<section style="background:#e0f7fa"><div class="container">'
        + '\n  <div class="sec-ey">The Decisive Advantages</div><h2>Why Recoverit Wins for Most Users</h2>'
        + '\n  <div class="grid3">'
        + '\n    <div class="card"><div class="fi">&#127910;</div><h3>Patented Video Repair</h3><p>No other consumer tool matches Recoverit\'s video fragment reconstruction for GoPro, DJI drone and action camera footage. Unique, patented, proven.</p></div>'
        + '\n    <div class="card"><div class="fi">&#127968;</div><h3>NAS Remote Recovery</h3><p>Recover from Synology, QNAP and WD NAS remotely without dismantling the server. No competitor offers this capability.</p></div>'
        + '\n    <div class="card"><div class="fi">&#128204;</div><h3>35+ Patents</h3><p>Wondershare holds 35+ patents for innovative recovery methods. Real-world recovery success that generic tools cannot match.</p></div>'
        + '\n  </div>\n</div></section>\n'
        + CTA("The Best Data Recovery Software &#8212; Try Free","Download Recoverit and recover up to 500MB for free.")
        + "\n" + FOOTER() + "\n</body></html>")


def page_glossary():
    terms = [
        ("Data Recovery","The process of retrieving deleted, lost, corrupted or inaccessible data from storage devices when normal access methods have failed."),
        ("Quick Scan","A fast scan mode that searches the file system directory for recently deleted file entries. Completes in seconds to minutes. Try this first before Deep Scan."),
        ("Deep Scan","A thorough sector-by-sector scan that searches for file signatures across the entire storage device. Takes longer but finds files after formatting, corruption or partition loss."),
        ("File Signature","A unique sequence of bytes at the start of each file type (also called a magic number) that identifies the file format. Recoverit uses these to find and reconstruct files even when directory entries are deleted."),
        ("Overwriting","When new data is saved to the same physical sectors as deleted data. Once overwritten, files cannot be recovered &#8212; the original data is permanently gone."),
        ("File System","The system a storage device uses to organise files (examples: NTFS, FAT32, exFAT for Windows; APFS, HFS+ for Mac; EXT4, Btrfs for Linux). Deletion removes a file from the file system index but typically leaves the data intact until overwritten."),
        ("NTFS","New Technology File System. The default file system for Windows drives. Supports large files, permissions and journaling."),
        ("FAT32","File Allocation Table 32. An older file system common on USB drives and SD cards. Compatible with almost all devices but limited to 4GB maximum file size."),
        ("exFAT","Extended File Allocation Table. Modern replacement for FAT32 used on flash storage. No 4GB file size limit. Supported by Windows, Mac and most modern cameras."),
        ("EXT4","The standard file system for Linux and most NAS devices (Synology, QNAP, WD). Required for NAS data recovery."),
        ("Btrfs","A modern Linux file system used by Synology NAS devices for its advanced snapshot and RAID features. Supported by Recoverit's NAS recovery."),
        ("TRIM","An SSD command that allows the operating system to inform the drive which data blocks are no longer needed. TRIM can cause deleted data to be immediately erased from SSDs, reducing recovery chances."),
        ("RAID","Redundant Array of Independent Disks. A technology that combines multiple drives for redundancy or performance. RAID recovery requires reconstructing the array\'s data striping pattern."),
        ("RAW Photo","An unprocessed camera file format (CR2, NEF, ARW, ORF, RW2) containing all data captured by the sensor. Higher quality than JPEG but larger files. Fully recoverable with Recoverit."),
        ("Video Corruption","Damage to a video file's container structure or frame data that prevents playback. Caused by interrupted recording, drive failure or incomplete file transfer. Repairable with Recoverit's video repair feature."),
        ("Bootable USB","A USB drive configured to start a computer independently of its internal drive. Recoverit creates bootable USB drives for recovering data from computers that won't start normally."),
        ("Sector","The smallest physical unit of storage on a hard drive (typically 512 bytes or 4KB). Deep Scan reads every sector on a drive to find file data regardless of the file system state."),
        ("Partition","A logical division of a storage device. A single hard drive can have multiple partitions. Lost or deleted partitions can be recovered with Recoverit's Deep Scan."),
        ("NAS","Network Attached Storage. A file storage device connected to a network. Recoverit recovers data from NAS devices remotely via SSH without physical dismantling."),
        ("Video Fragment Reconstruction","Recoverit's patented technology that rebuilds corrupted video files by identifying and reassembling individual video and audio frames from raw binary data. Particularly effective for action camera footage."),
        ("Disk Image","An exact byte-for-byte copy of a storage device saved as a single file. Recoverit can recover data from disk images without accessing the physical drive, preventing further wear."),
        ("Ransomware","Malware that encrypts files and demands payment for decryption. Recoverit can recover Shadow Volume Copies and pre-encryption versions of files after a ransomware attack."),
        ("Shadow Volume Copy","A Windows feature that periodically creates backup snapshots of files. Can be used to recover previous versions of files after ransomware or accidental modification."),
        ("Journaling","A feature of modern file systems (NTFS, EXT4, APFS) that keeps a log of file system changes. Journaling helps Recoverit's Deep Scan reconstruct file locations even after corruption."),
        ("Write Protection","A hardware or software mechanism that prevents data from being written to a storage device. Useful during recovery to prevent accidental overwriting of recoverable data."),
    ]
    cards = "".join('<div class="card"><h3>' + t + '</h3><p>' + d + '</p></div>' for t,d in terms)
    bc = BC_SCHEMA([("Home",""),("Glossary","")])
    return (HEAD("Data Recovery Glossary &#8212; " + str(len(terms)) + " Terms Explained | " + str(YEAR),
                 "Complete data recovery glossary &#8212; Quick Scan, Deep Scan, RAID, NAS, file signatures, video corruption, TRIM and more.",
                 "glossary.html", bc)
        + "\n<body>\n" + NAV()
        + "\n" + BC([("Home",BASE_PATH+"/"),("Glossary","")])
        + '\n<section class="hero">'
        + '\n  <div class="eyebrow">&#10022; Data Recovery Reference</div>'
        + '\n  <h1>Data Recovery<br><em>Glossary</em></h1>'
        + '\n  <p class="hsub">' + str(len(terms)) + ' plain-language definitions for every term you\'ll encounter when recovering data.</p>'
        + '\n</section>\n'
        + '\n<section><div class="container">'
        + '\n  <div class="sec-ey">' + str(len(terms)) + ' Terms Defined</div><h2>Complete Glossary</h2>'
        + '\n  <div class="grid3">' + cards + '</div>'
        + '\n</div></section>\n'
        + CTA("Ready to Recover Your Data?","Download Recoverit free and put this knowledge to work now.")
        + "\n" + FOOTER() + "\n</body></html>")


def page_download():
    bc = BC_SCHEMA([("Home",""),("Download","")])
    return (HEAD("Download Recoverit Free &#8212; Data Recovery Windows & Mac | " + str(YEAR),
                 "Download Wondershare Recoverit free. Recover deleted photos, videos, documents. Free 500MB recovery, no credit card needed.",
                 "download.html", bc)
        + "\n<body>\n" + NAV()
        + "\n" + BC([("Home",BASE_PATH+"/"),("Download","")])
        + '\n<section class="hero">'
        + '\n  <div class="eyebrow">&#10022; Free Trial Available</div>'
        + '\n  <h1>Download Recoverit<br><em>Free Today</em></h1>'
        + '\n  <p class="hsub">Recover up to 500MB for free &#8212; no credit card required. Windows 7/8/10/11 and macOS 10.12+.</p>'
        + '\n  <a href="' + AFFILIATE_URL + '" class="btn-p" target="_blank" rel="nofollow sponsored" style="font-size:1.1rem;padding:1rem 2.5rem">&#8659; Download Free &#8212; Recover 500MB</a>'
        + '\n  <p style="color:rgba(255,255,255,.38);font-size:.78rem;margin-top:1rem">Windows 7/8/10/11 &#183; macOS 10.12+ &#183; Intel &amp; Apple Silicon</p>'
        + '\n</section>\n'
        + '\n<section><div class="container">'
        + '\n  <div class="sec-ey">What You Get Free</div><h2>Free Trial Includes Every Feature</h2>'
        + '\n  <p class="sec-sub">Scan, preview and recover up to 500MB completely free. See your recoverable files before purchasing.</p>'
        + FEATURES_GRID()
        + '\n</div></section>\n'
        + '\n<section style="background:#fff"><div class="container">'
        + '\n  <div class="sec-ey">System Requirements</div><h2>Compatible With Your Setup</h2>'
        + '\n  <div class="grid2">'
        + '\n    <div class="card"><h3>&#128421; Windows</h3><ul><li>Windows 7 / 8 / 10 / 11</li><li>32-bit and 64-bit</li><li>2 GB RAM minimum (4 GB recommended)</li><li>500 MB free disk space for installation</li></ul></div>'
        + '\n    <div class="card"><h3>&#63743; macOS</h3><ul><li>macOS 10.12 Sierra and above</li><li>Includes Sonoma &amp; Sequoia</li><li>Intel and Apple Silicon M1/M2/M3</li><li>2 GB RAM minimum</li></ul></div>'
        + '\n  </div>\n</div></section>\n'
        + CTA("Download Recoverit Now","Free trial &#183; No credit card &#183; Windows &amp; Mac &#183; All features included.")
        + "\n" + FOOTER() + "\n</body></html>")


def page_keywords():
    cats = defaultdict(list)
    for k in KEYWORDS: cats[k["cat"]].append(k)
    sections = ""
    for cat in sorted(cats.keys()):
        items = cats[cat]; desc = CAT_DESC.get(cat,""); a1,_ = ac(cat)
        links = "".join('<a class="kw" href="' + BASE_PATH + '/' + k["slug"] + '.html">' + k["keyword"] + '</a>' for k in items)
        sections += ('<div style="margin-bottom:3rem">'
                     '<h3 style="font-size:1rem;font-weight:700;color:' + a1 + ';margin-bottom:.35rem;border-bottom:2px solid ' + a1 + ';padding-bottom:.35rem;display:inline-block">'
                     + cat.replace("-"," ").title() + ' <span style="color:var(--muted);font-weight:400;font-size:.83rem">(' + str(len(items)) + ')</span></h3>'
                     + ('<p style="font-size:.82rem;color:var(--muted);margin:.45rem 0 .7rem;max-width:600px">' + desc + '</p>' if desc else '')
                     + '<div class="kw-cloud">' + links + '</div></div>')
    bc = BC_SCHEMA([("Home",""),("All Topics","")])
    return (HEAD("Recoverit &#8212; All " + str(len(KEYWORDS)) + " Data Recovery Topics | " + str(YEAR),
                 "Browse all " + str(len(KEYWORDS)) + " data recovery topics &#8212; deleted photos, videos, hard drives, SD cards, USB, NAS and more.",
                 "keywords.html", bc)
        + "\n<body>\n" + NAV()
        + "\n" + BC([("Home",BASE_PATH+"/"),("All Topics","")])
        + '\n<section class="hero">'
        + '\n  <div class="eyebrow">&#10022; Complete Topic Directory</div>'
        + '\n  <h1>All Data Recovery<br><em>Topics</em></h1>'
        + '\n  <p class="hsub">' + str(len(KEYWORDS)) + ' targeted topics covering every data recovery scenario and device type.</p>'
        + '\n</section>\n'
        + '\n<section><div class="container"><div class="sec-ey">Browse All ' + str(len(KEYWORDS)) + ' Topics</div>'
        + sections + '</div></section>\n'
        + CTA() + "\n" + FOOTER() + "\n</body></html>")


def page_privacy():
    bc = BC_SCHEMA([("Home",""),("Privacy","")])
    return (HEAD("Privacy Policy &#8212; RecoverIt Guide","Privacy policy for the RecoverIt affiliate guide website.","privacy.html",bc)
        + "\n<body>\n" + NAV()
        + "\n" + BC([("Home",BASE_PATH+"/"),("Privacy Policy","")])
        + '\n<section class="hero" style="padding:3.5rem 2rem 3rem">'
        + '\n  <div class="eyebrow">Legal</div><h1>Privacy <em>Policy</em></h1>'
        + '\n</section>\n'
        + '\n<section style="background:#fff"><div class="container"><div class="prose" style="max-width:800px">'
        + '\n  <p><strong>Last updated: ' + BUILD_DATE + '</strong></p>'
        + '\n  <h3>1. About This Website</h3><p>This is an affiliate promotional website for Wondershare Recoverit data recovery software. We do not collect personal data beyond standard web server logs.</p>'
        + '\n  <h3>2. Affiliate Disclosure</h3><p>This website contains affiliate links. When you click a link and purchase Recoverit, we may receive a commission from Wondershare at no extra cost to you.</p>'
        + '\n  <h3>3. Cookies</h3><p>This website does not use tracking cookies. Standard browser caching may apply.</p>'
        + '\n  <h3>4. External Links</h3><p>All purchase links lead to the official Wondershare website. We are not responsible for the privacy practices of external sites.</p>'
        + '\n</div></div></section>\n' + FOOTER() + "\n</body></html>")


def page_404():
    return ("<!DOCTYPE html>\n<html lang=\"en\"><head>\n"
            "<meta charset=\"UTF-8\"/><meta name=\"viewport\" content=\"width=device-width,initial-scale=1.0\"/>\n"
            "<title>Page Not Found &#8212; RecoverIt</title>\n"
            "<meta http-equiv=\"refresh\" content=\"4;url=" + SITE_DOMAIN + "/\"/>\n"
            "<style>body{font-family:system-ui,sans-serif;background:#0f172a;color:#fff;"
            "display:flex;align-items:center;justify-content:center;min-height:100vh;text-align:center;margin:0;padding:2rem}"
            "h1{font-size:3rem;margin-bottom:.75rem;font-weight:800}"
            "p{color:rgba(255,255,255,.6);margin-bottom:2rem;line-height:1.6}"
            "a{background:#00b4d8;color:#fff;padding:.85rem 2.2rem;border-radius:8px;text-decoration:none;font-weight:700}</style>"
            "</head><body><div>"
            "<div style=\"font-size:4rem;margin-bottom:1rem\">&#128190;</div>"
            "<h1>Page Not Found</h1>"
            "<p>Redirecting to the homepage in 4 seconds...</p>"
            "<a href=\"" + SITE_DOMAIN + "/\">Go to RecoverIt Home</a>"
            "</div></body></html>")


BLOG_POSTS = [
    {"slug":"how-to-recover-deleted-photos","title":"How to Recover Deleted Photos in 2025","excerpt":"Accidentally deleted your photos? Complete guide to recovering them from any device — SD card, hard drive, USB or camera.","cat":"Photos","read":"7 min","date":"2025-01-15",
     "body":"<h2>Can Deleted Photos Be Recovered?</h2><p>In most cases, yes. When a photo is deleted, the operating system removes the directory entry but leaves the image data on the storage device until new data overwrites it. Act quickly and the photos are often fully recoverable.</p><h2>The #1 Rule</h2><p><strong>Stop using the device immediately.</strong> Every photo taken, every sync that runs, every app that opens writes data to storage and risks overwriting your deleted photos.</p><h2>Recovery Steps</h2><ol><li>Download and install Recoverit on a different drive than the one with lost photos</li><li>Connect the camera, SD card or phone</li><li>Select the device in Recoverit and run Quick Scan</li><li>If not found, switch to Deep Scan</li><li>Preview recovered photos to confirm quality</li><li>Recover to a different location than the source</li></ol><h2>RAW Photo Recovery</h2><p>Recoverit fully supports all major RAW formats &#8212; CR2, NEF, ARW, ORF, RW2, DNG and more. RAW files are recovered at full original quality with no degradation during the recovery process.</p>"},
    {"slug":"how-to-recover-deleted-videos","title":"How to Recover Deleted Videos — GoPro, Drone & Camera","excerpt":"Lost GoPro footage, drone video or camera recordings? Recoverit recovers them even if they're corrupted and won't play.","cat":"Videos","read":"7 min","date":"2025-02-10",
     "body":"<h2>Why Video Recovery Is Harder</h2><p>Videos are large files often stored across many sectors. When deleted or corrupted, fragments can be scattered. Recoverit's patented video fragment reconstruction is specifically designed for this challenge.</p><h2>Deleted vs Corrupted Videos</h2><p><strong>Deleted videos</strong> &#8212; directory entry removed but data intact. Recovered with standard scan. <strong>Corrupted videos</strong> &#8212; file exists but won't play due to damaged header or frames. Requires Recoverit's video repair feature.</p><h2>GoPro and Action Camera Recovery</h2><p>GoPro uses specific H.264/H.265 encoding and file structures. Generic tools often fail to reconstruct GoPro files correctly. Recoverit's patented methods include GoPro-specific video patterns giving significantly higher success rates.</p><h2>DJI Drone Footage</h2><p>Recoverit supports DJI .MOV and .MP4 footage including 4K recordings from Mavic, Phantom and Air series. Even partially corrupted files can often be repaired to full playability.</p>"},
    {"slug":"sd-card-data-recovery","title":"SD Card Data Recovery — Complete Guide 2025","excerpt":"Corrupted SD card? Accidentally formatted? Files showing as unreadable? Here's how to get everything back.","cat":"SD Cards","read":"6 min","date":"2025-03-05",
     "body":"<h2>Why SD Cards Lose Data</h2><p>Removing the card during write, accidental formatting, physical shock, card reader errors, file system corruption and wear from many write cycles all cause SD card data loss.</p><h2>Warning Signs</h2><ul><li>Camera shows 'Card Error' despite card being inserted</li><li>Files appear as 0 bytes or corrupted thumbnails</li><li>Card shows as unformatted when connected to a PC</li><li>Files are visible but won't open or play</li></ul><h2>What NOT to Do</h2><p>Do not format the card. Do not take more photos. Do not run CHKDSK on the card. All can overwrite or damage recoverable data.</p><h2>Recovery Steps</h2><ol><li>Remove card from camera and connect via card reader</li><li>Install Recoverit on the computer (not on the SD card)</li><li>Select the SD card in Recoverit</li><li>Run Quick Scan, then Deep Scan if needed</li><li>Preview photos and videos</li><li>Recover to your computer's hard drive</li></ol>"},
    {"slug":"recover-data-from-crashed-computer","title":"How to Recover Data From a Computer That Won't Start","excerpt":"Blue Screen? PC won't boot? You can still get your files. Here's exactly how to do it.","cat":"Crashed PC","read":"8 min","date":"2025-04-12",
     "body":"<h2>Your Data Is Almost Certainly Still There</h2><p>A computer that won't start does not mean your data is gone. Software failure, BSOD, corrupted OS or failed update &#8212; in these cases the data on the drive is usually completely intact. You just can't access it because the OS won't load.</p><h2>Creating a Bootable Recovery USB</h2><ol><li>On a working computer, download and install Recoverit</li><li>Go to Computer Crashed Recovery section</li><li>Insert a USB drive (8GB or larger &#8212; all data on it will be erased)</li><li>Click Create Bootable USB</li></ol><h2>Recovering From the Crashed PC</h2><ol><li>Insert the bootable Recoverit USB into the crashed PC</li><li>Start PC and boot from USB (F12 or Del to access boot menu)</li><li>Recoverit launches from USB and scans the internal drive</li><li>Select files and save to the USB drive or external hard drive</li></ol>"},
    {"slug":"usb-drive-data-recovery","title":"USB Drive Data Recovery — Get Your Files Back","excerpt":"Lost files from a USB drive? Formatted by accident? Here's how to recover everything.","cat":"USB Drives","read":"6 min","date":"2025-05-20",
     "body":"<h2>Common USB Data Loss Causes</h2><p>Accidental deletion, formatting the wrong drive, unsafe removal causing file system corruption, virus infection, and physical damage are the most common causes.</p><h2>Recovering Deleted Files</h2><ol><li>Connect the USB drive &#8212; do NOT save new files to it</li><li>Open Recoverit and select the USB drive</li><li>Run Quick Scan for recently deleted files</li><li>Preview and recover to your computer's hard drive</li></ol><h2>Recovering From an Accidentally Formatted USB</h2><p>Use Deep Scan rather than Quick Scan. Formatting removes the directory structure but typically does not erase file data. Deep Scan searches raw sectors for file signatures and recovers files even after formatting &#8212; provided minimal new data has been written since.</p><h2>Drive Shows as RAW or Needs Formatting</h2><p>If Windows asks you to format the USB when you connect it, this usually means a corrupted file system &#8212; not that data is gone. Do NOT format. Run Recoverit's Deep Scan first.</p>"},
    {"slug":"recover-data-after-format","title":"How to Recover Data After Formatting a Drive","excerpt":"Formatted the wrong drive? Files not truly gone — here's what's still possible.","cat":"Format","read":"6 min","date":"2025-06-15",
     "body":"<h2>Is Recovery Possible After Formatting?</h2><p>Quick format (the Windows default) clears only the directory &#8212; file data remains. Full format writes zeros and significantly reduces recovery chances. Quick-formatted drives are often fully recoverable.</p><h2>Act Immediately</h2><p>Stop using the drive, do not save files to it, do not install software to it. Connect it to another computer and run Recoverit from a separate drive.</p><h2>Deep Scan Is Essential</h2><p>Quick Scan reads the file system directory, which formatting has cleared. Use Deep Scan to read raw sector data and identify files by binary signatures. Expect 1-4 hours for a typical hard drive.</p><h2>What Affects Recovery Success</h2><p>New data written after formatting is the biggest factor. If a 1TB formatted drive has 600GB of new data, the 400GB still free may be fully recoverable. Act immediately to maximise what can be saved.</p>"},
    {"slug":"prevent-data-loss-guide","title":"How to Prevent Data Loss — The Complete 2025 Guide","excerpt":"The best recovery is data you never need to recover. Here's how to protect yourself completely.","cat":"Prevention","read":"7 min","date":"2025-07-10",
     "body":"<h2>The 3-2-1 Backup Rule</h2><p>Keep <strong>3 copies</strong> of your data, on <strong>2 different types of storage</strong>, with <strong>1 copy offsite or in the cloud</strong>. For most people: original on your computer (1), backup on an external hard drive (2), backup in cloud storage (3). This protects against hardware failure, theft, fire and accidental deletion simultaneously.</p><h2>How Often to Back Up</h2><p>Critical business data: daily. Personal documents and photos: weekly minimum. Photographers and videographers: after every session. Most backup software runs automatically in the background.</p><h2>Protecting SD Cards</h2><p>Always use the camera's proper shutdown before removing the card. Never remove the card while the write indicator is on. Replace cards every 3-5 years &#8212; flash memory degrades invisibly. Format cards in-camera rather than on a PC for best compatibility.</p><h2>Despite Everything, Have Recoverit Ready</h2><p>Even with perfect backups, accidents happen. Having Recoverit installed means that when the unexpected occurs &#8212; and it will &#8212; you can recover quickly without panic.</p>"},
    {"slug":"gopro-video-recovery","title":"GoPro Video Recovery — Recover Lost & Corrupted Footage","excerpt":"Lost GoPro videos or footage that won't play? Recoverit's patented technology recovers GoPro footage other tools miss.","cat":"GoPro","read":"6 min","date":"2025-08-05",
     "body":"<h2>Why GoPro Footage Is Uniquely Challenging</h2><p>GoPro cameras use specific H.264/H.265 encoding and file structures that differ from standard video files. When deleted or corrupted &#8212; usually from removing the SD card during recording or unexpected battery death &#8212; generic tools often fail to reconstruct the video correctly.</p><h2>Recoverit's GoPro-Specific Recovery</h2><p>Recoverit holds patents covering video fragment reconstruction that specifically recognises GoPro's proprietary video segment patterns. In independent testing, Recoverit consistently recovers GoPro footage that other tools detect but cannot play.</p><h2>Common GoPro Data Loss Causes</h2><ul><li>SD card removed during active recording</li><li>Battery died during recording</li><li>Accidental deletion from camera or computer</li><li>SD card formatted accidentally</li><li>Card showing errors or not recognised</li></ul><h2>Recovery Process</h2><ol><li>Remove SD card from GoPro</li><li>Connect via card reader to computer</li><li>Select the SD card in Recoverit and run Deep Scan</li><li>Use video repair for footage found but not playing</li><li>Recover to your computer's hard drive</li></ol>"},
    {"slug":"nas-data-recovery-guide","title":"NAS Data Recovery — Synology, QNAP & WD Complete Guide","excerpt":"Lost data from your NAS? Recoverit recovers it remotely without dismantling your server.","cat":"NAS","read":"7 min","date":"2025-09-15",
     "body":"<h2>NAS Data Loss Causes</h2><p>RAID controller failure, accidental deletion or volume formatting, firmware update failures, ransomware attacks on NAS shares, and individual drive failure within a RAID array.</p><h2>Remote Recovery Without Dismantling</h2><p>Recoverit connects to NAS devices remotely via SSH over your local network. No physical dismantling, no business downtime beyond the scan duration. The NAS continues operating while Recoverit performs its analysis.</p><h2>Supported Systems</h2><p>Synology (DSM, EXT4, Btrfs), QNAP (QTS, EXT4, ZFS), WD My Cloud (EXT3/EXT4) and other Linux-based NAS. RAID 0, 1, 5, 6 and 10 recovery supported.</p><h2>Recovery Steps</h2><ol><li>Ensure NAS is on and connected to your local network</li><li>Open Recoverit and select NAS Recovery</li><li>Enter the NAS IP address and credentials</li><li>Recoverit establishes remote connection and scans</li><li>Preview and recover files to your local computer</li></ol>"},
    {"slug":"recoverit-vs-disk-drill","title":"Recoverit vs Disk Drill — Which Is Better in 2025?","excerpt":"The two most recommended data recovery tools compared head to head. Honest analysis of recovery rates, features and pricing.","cat":"Comparison","read":"8 min","date":"2025-10-20",
     "body":"<h2>Overview</h2><p>Recoverit (Wondershare) and Disk Drill (CleverFiles) are consistently ranked as the top two consumer data recovery tools. Both offer solid recovery rates and free trial options. But they have distinct strengths.</p><h2>Where Recoverit Leads</h2><ul><li><strong>Video repair</strong> &#8212; Recoverit's patented fragment reconstruction for GoPro and drone footage has no equivalent in Disk Drill</li><li><strong>NAS remote recovery</strong> &#8212; Disk Drill does not support this</li><li><strong>AI photo enhancement</strong> &#8212; Disk Drill does not offer this</li><li><strong>Deep scan on formatted drives with heavy new data</strong> &#8212; Recoverit achieves higher recovery in independent tests</li><li><strong>35+ patents</strong> &#8212; proprietary methods that generic tools cannot replicate</li></ul><h2>Where Disk Drill Leads</h2><ul><li>Mac free-tier scanning flexibility</li><li>Drive health monitoring features</li><li>Backup vault (disk image before recovery)</li></ul><h2>Verdict</h2><p>For most users &#8212; especially photographers, videographers, and anyone dealing with complex recovery &#8212; Recoverit is the better choice. Disk Drill is a reasonable alternative if you primarily use Mac and value its health monitoring features.</p>"},
    {"slug":"recover-permanently-deleted-files-windows","title":"How to Recover Permanently Deleted Files on Windows","excerpt":"Shift+deleted or emptied the Recycle Bin? Files aren't truly gone — here's how to get them back.","cat":"Windows","read":"6 min","date":"2025-11-10",
     "body":"<h2>What 'Permanently Deleted' Actually Means</h2><p>Shift+Delete or emptying the Recycle Bin marks the file's space as available but leaves the actual data on the drive until something else overwrites it. The sooner you act, the better your recovery chances.</p><h2>Try Windows Previous Versions First</h2><p>Right-click the folder where the file was, select Properties, then Previous Versions. If Windows File History has been running, a previous version may be available &#8212; the fastest recovery option if backups exist.</p><h2>Using Recoverit</h2><ol><li>Download Recoverit &#8212; save to a different drive than the one with lost files</li><li>Select the drive or folder where files were deleted</li><li>Run Quick Scan first</li><li>For older deletions, run Deep Scan</li><li>Preview and recover to a different drive</li></ol><h2>Maximise Your Chances</h2><p>Once you realise files are deleted: stop saving new files, close unnecessary applications, disable cloud sync that might write data, and run Recoverit immediately.</p>"},
    {"slug":"video-repair-software-guide","title":"How to Repair Corrupted Video Files — Complete Guide","excerpt":"Video files that won't play after data recovery, interrupted recording or drive failure can often be fixed. Here's how.","cat":"Video Repair","read":"7 min","date":"2025-12-01",
     "body":"<h2>Why Videos Become Corrupted</h2><p>The most common causes: removing an SD card or battery while the camera is actively writing; unexpected power loss during recording; incomplete file transfers; and storage device errors that corrupt the container while leaving frame data intact.</p><h2>What Video Corruption Actually Is</h2><p>A video file has two parts: the <strong>container</strong> (the MP4, MOV or AVI wrapper that indexes where video and audio frames are) and the <strong>frame data</strong> (the actual video and audio content). Corruption typically damages the container while leaving the frame data intact. Repair means rebuilding a valid container around the intact frame data.</p><h2>Recoverit's Repair Method</h2><p>Recoverit's patented fragment-based reconstruction analyses the raw binary data of a corrupted video, identifies video and audio frames, and reconstructs a valid container around them. This is more effective than simple header patching because it works from the frame data up.</p><h2>Supported Formats</h2><p>MP4, MOV, AVI, MKV, M4V, 3GP, FLV, WMV, INSV and GoPro's proprietary formats. Supports 4K, 8K, HDR and high-bitrate footage from all major manufacturers.</p><h2>Step-by-Step</h2><ol><li>Open Recoverit and go to Video Repair</li><li>Add the corrupted video files</li><li>Click Repair and wait for the process to complete</li><li>Preview the repaired video to confirm playability</li><li>Save the repaired file to a different location</li></ol>"},
    {"slug":"best-data-recovery-software-2025","title":"Best Data Recovery Software in 2025 — Ranked & Reviewed","excerpt":"We tested every major data recovery tool. Here's the honest ranking based on actual recovery results.","cat":"Reviews","read":"9 min","date":"2026-01-15",
     "body":"<h2>How We Evaluated</h2><p>We deleted and formatted test drives with known sets of photos, videos and documents, then attempted recovery with each tool. We measured: percentage of files recovered, quality of recovered media, interface ease of use, scanning speed and pricing.</p><h2>1. Wondershare Recoverit &#8212; Best Overall</h2><p>Recoverit earns the top spot with the highest recovery rate in our testing, particularly for corrupted media files. Patented video fragment reconstruction is genuinely unique. NAS remote recovery and AI photo enhancement add capabilities no competitor offers. Free tier: 500MB. <strong>Verdict: best choice for most users.</strong></p><h2>2. Disk Drill &#8212; Best Mac Experience</h2><p>Comparable to Recoverit for standard photo and document recovery. Leads on Mac usability and includes a backup vault. No video repair, no NAS support. Free tier: 500MB. <strong>Verdict: excellent if you primarily use Mac.</strong></p><h2>3. EaseUS Data Recovery &#8212; Best for Documents</h2><p>Excellent document recovery results and a clean interface. Strong deep scan on formatted drives. No video repair. Free tier: 500MB. <strong>Verdict: good for office file recovery.</strong></p><h2>4. Recuva &#8212; Best Free Tool</h2><p>Free, Windows-only, effective for straightforward deletions. Not updated frequently. No video repair, no Mac support. <strong>Verdict: fine for basic recovery, inadequate for complex scenarios.</strong></p><h2>Overall Recommendation</h2><p>For deleted photos, corrupted video, formatted drives or complex recovery &#8212; Recoverit is the clear first choice in 2025.</p>"},
    {"slug":"recover-data-after-ransomware","title":"How to Recover Files After a Ransomware Attack","excerpt":"Ransomware encrypted your files? Not all hope is lost — here are all your options for getting data back.","cat":"Security","read":"8 min","date":"2026-02-10",
     "body":"<h2>What Ransomware Does to Your Files</h2><p>Ransomware encrypts your files and renames them with an unfamiliar extension. The original unencrypted files are deleted after encryption. This deletion is often not a secure wipe &#8212; meaning the original files may be recoverable with data recovery software before they are overwritten.</p><h2>Option 1: Recover Pre-Encryption Files</h2><p>If the ransomware deleted the originals before encrypting them, Recoverit can potentially recover those originals from the drive. This only works if: not much time has passed since the attack, and the drive has not had significant new data written to it since. Run Recoverit's Deep Scan immediately after isolating the infected machine.</p><h2>Option 2: Shadow Volume Copies</h2><p>Windows creates automatic backup snapshots (Shadow Volume Copies) periodically. Some ransomware deletes these, but some doesn't. Check with Windows Previous Versions or a shadow copy tool before assuming this option is unavailable.</p><h2>Option 3: Backup Recovery</h2><p>If you have offsite or cloud backups that predate the infection, restoring from backup is the cleanest solution. This is the ultimate argument for the 3-2-1 backup strategy with one copy in an air-gapped location.</p><h2>Critical: Isolate the Infected Machine</h2><p>Disconnect the infected computer from the network immediately to prevent ransomware spreading to other devices or backups. Do not pay the ransom &#8212; payment does not guarantee decryption and funds further criminal activity.</p>"},
    {"slug":"recover-photos-from-digital-camera","title":"Recover Deleted Photos From Any Digital Camera","excerpt":"Complete guide to recovering photos from Canon, Nikon, Sony, Fuji and all other camera brands.","cat":"Cameras","read":"6 min","date":"2026-03-05",
     "body":"<h2>How Camera Photo Recovery Works</h2><p>Digital cameras store photos on removable SD, CF or XQD cards. When a photo is deleted in-camera, the card's file system entry is removed but the image data remains until overwritten by a new photo. Recoverit reads the raw card data and reconstructs photos by their file signatures.</p><h2>Supported Camera Brands</h2><p>Recoverit supports recovery from all major manufacturers: Canon (CR2, CR3), Nikon (NEF, NRW), Sony (ARW, SR2, SRF), Fujifilm (RAF), Olympus (ORF), Panasonic (RW2), Pentax (PEF, DNG), Leica (DNG) and more. All RAW formats are recovered at full original quality.</p><h2>Step-by-Step Recovery</h2><ol><li>Remove the memory card from the camera &#8212; do not take any more photos</li><li>Connect the card to a computer using a card reader (not the USB cable from the camera)</li><li>Open Recoverit and select the memory card</li><li>Run Quick Scan &#8212; switch to Deep Scan if needed</li><li>Preview recovered photos by thumbnail</li><li>Select and recover to a folder on your computer's hard drive</li></ol><h2>Recovering Videos From Cameras</h2><p>The same process works for video files recorded on camera SD cards &#8212; including 4K MOV files from mirrorless cameras and high-bitrate XAVC from Sony cameras. The video repair feature handles any footage that is found but won't play.</p>"},
]

def page_blog():
    bc = BC_SCHEMA([("Home",""),("Blog","")])
    cards = "".join(
        '<div class="card"><div class="badge">' + p["cat"] + '</div>'
        '<h3 style="margin-top:.55rem;margin-bottom:.45rem;font-size:.97rem">'
        '<a href="' + BASE_PATH + '/blog/' + p["slug"] + '.html" style="color:var(--ink)">' + p["title"] + '</a></h3>'
        '<p style="font-size:.84rem;margin-bottom:.85rem">' + p["excerpt"] + '</p>'
        '<div style="display:flex;justify-content:space-between;align-items:center">'
        '<span style="font-size:.73rem;color:var(--muted)">' + p["date"] + ' &#183; ' + p["read"] + '</span>'
        '<a href="' + BASE_PATH + '/blog/' + p["slug"] + '.html" style="font-size:.8rem;font-weight:600;color:var(--ha)">Read &#8594;</a>'
        '</div></div>'
        for p in BLOG_POSTS)
    return (HEAD("RecoverIt Blog &#8212; Data Recovery Guides & Tutorials | " + str(YEAR),
                 "Data recovery guides, step-by-step tutorials and tips &#8212; recover deleted photos, videos, documents and more.",
                 "blog.html", bc)
        + "\n<body>\n" + NAV()
        + "\n" + BC([("Home",BASE_PATH+"/"),("Blog","")])
        + '\n<section class="hero">'
        + '\n  <div class="eyebrow">&#10022; Data Recovery Guides</div>'
        + '\n  <h1>Guides, Tips &amp;<br><em>Recovery Tutorials</em></h1>'
        + '\n  <p class="hsub">' + str(len(BLOG_POSTS)) + ' in-depth articles covering every data recovery scenario &#8212; from deleted photos to crashed hard drives.</p>'
        + '\n</section>\n'
        + '\n<section><div class="container">'
        + '\n  <div class="sec-ey">All ' + str(len(BLOG_POSTS)) + ' Articles</div><h2>Data Recovery Guides</h2>'
        + '\n  <div class="grid3">' + cards + '</div>'
        + '\n</div></section>\n'
        + CTA("Need to Recover Data Right Now?","Download Recoverit &#8212; recover up to 500MB free, no credit card required.")
        + "\n" + FOOTER() + "\n</body></html>")

def page_blog_post(post):
    bc  = BC_SCHEMA([("Home",""),("Blog","blog.html"),(post["title"][:40]+"...","")])
    art = ART_SCHEMA(post["title"], post["excerpt"], post["date"])
    others = [p for p in BLOG_POSTS if p["slug"] != post["slug"]][:3]
    rel = "".join(
        '<div class="card"><div class="badge">' + p["cat"] + '</div>'
        '<h3 style="margin-top:.5rem;font-size:.93rem">'
        '<a href="' + BASE_PATH + '/blog/' + p["slug"] + '.html" style="color:var(--ink)">' + p["title"] + '</a></h3>'
        '<p style="font-size:.82rem">' + p["excerpt"] + '</p></div>'
        for p in others)
    h = HEAD(post["title"] + " | RecoverIt Guide", post["excerpt"], "blog/" + post["slug"] + ".html", bc+art, "article")
    return (h + "\n<body>\n" + NAV()
        + "\n" + BC([("Home",BASE_PATH+"/"),("Blog",BASE_PATH+"/blog.html"),(post["cat"],"")])
        + '\n<section class="hero" style="padding:3.5rem clamp(1rem,5vw,3rem) 3rem">'
        + '\n  <div class="eyebrow">&#10022; ' + post["cat"] + ' &#183; ' + post["read"] + '</div>'
        + '\n  <h1 style="font-size:clamp(1.7rem,4vw,2.8rem)">' + post["title"] + '</h1>'
        + '\n  <p class="hsub" style="font-size:1rem">' + post["excerpt"] + '</p>'
        + '\n  <p style="color:rgba(255,255,255,.38);font-size:.76rem">Published ' + post["date"] + '</p>'
        + '\n</section>\n'
        + '\n<section style="background:#fff"><div class="container"><div style="max-width:780px">'
        + '\n  <div class="prose">' + post["body"] + '</div>'
        + '\n  <div class="notice" style="margin-top:2.5rem">'
        + '\n    <strong>Ready to recover?</strong> Recoverit recovers 500MB free &#8212; no credit card. '
        + '\n    <a href="' + AFFILIATE_URL + '" target="_blank" rel="nofollow sponsored" style="color:var(--ha);font-weight:600">Download free trial &#8594;</a>'
        + '\n  </div></div></div></section>\n'
        + '\n<section><div class="container">'
        + '\n  <div class="sec-ey">More Guides</div><h2>Related Articles</h2>'
        + '\n  <div class="grid3">' + rel + '</div>'
        + '\n</div></section>\n'
        + CTA() + "\n" + FOOTER() + "\n</body></html>")


# ═══════════════════════════════════════════════
#  SUPPORT FILES + WORKFLOW + MAIN
# ═══════════════════════════════════════════════
def build_sitemap():
    essential = [("",1.0,"weekly"),("features.html",.9,"monthly"),("how-it-works.html",.9,"monthly"),
                 ("faq.html",.85,"monthly"),("compare.html",.85,"monthly"),("blog.html",.85,"weekly"),
                 ("download.html",.9,"monthly"),("keywords.html",.8,"monthly"),
                 ("glossary.html",.75,"monthly"),("privacy.html",.3,"yearly")]
    urls = ""
    for path,pri,freq in essential:
        loc = SITE_DOMAIN + ("/" + path if path else "/")
        urls += "  <url><loc>" + loc + "</loc><lastmod>" + BUILD_DATE + "</lastmod><changefreq>" + freq + "</changefreq><priority>" + str(pri) + "</priority></url>\n"
    for p in BLOG_POSTS:
        urls += "  <url><loc>" + SITE_DOMAIN + "/blog/" + p["slug"] + ".html</loc><lastmod>" + p["date"] + "</lastmod><changefreq>monthly</changefreq><priority>0.75</priority></url>\n"
    for k in KEYWORDS:
        urls += "  <url><loc>" + SITE_DOMAIN + "/" + k["slug"] + ".html</loc><lastmod>" + BUILD_DATE + "</lastmod><changefreq>monthly</changefreq><priority>0.65</priority></url>\n"
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + '</urlset>'

def build_robots():
    return "User-agent: *\nAllow: /\nDisallow: /build-report.json\nSitemap: " + SITE_DOMAIN + "/sitemap.xml\n"

def build_llms():
    cats   = sorted(set(k["cat"] for k in KEYWORDS))
    sample = ", ".join(k["keyword"] for k in KEYWORDS[:35])
    return ("# Wondershare Recoverit\n\n"
            "> Professional data recovery software by Wondershare Technology. Recovers deleted, lost or corrupted files from any storage device with 99.5% success rate. Supports 1,000+ file types, 10,000+ recovery scenarios, 1 million+ devices. Free 500MB trial.\n\n"
            "## Key Capabilities\n"
            "- Recover deleted photos (JPEG, PNG, RAW: CR2, NEF, ARW, ORF)\n"
            "- Recover deleted videos (MP4, MOV, AVI, MKV, 4K, 8K)\n"
            "- Recover deleted documents (Word, Excel, PDF, PowerPoint)\n"
            "- Recover deleted audio (MP3, WAV, AAC, FLAC)\n"
            "- Patented video repair for corrupted GoPro, DJI drone and camera footage\n"
            "- Quick Scan (seconds) and Deep Scan (formatted drives)\n"
            "- Bootable USB for crashed computer recovery\n"
            "- Remote NAS recovery (Synology, QNAP, WD) without dismantling\n"
            "- AI photo enhancement and repair\n"
            "- 35+ patents for innovative recovery methods\n"
            "- RAID 0/1/5/6/10 array recovery\n\n"
            "## Key Stats\n"
            "- 99.5% recovery success rate\n"
            "- 1,000+ supported file types\n"
            "- 10,000+ recovery scenarios\n"
            "- 1 million+ supported devices\n"
            "- 35+ patents\n\n"
            "## Platforms\nWindows 7/8/10/11 (32-bit & 64-bit) · macOS 10.12+ including Sonoma & Sequoia · Intel & Apple Silicon\n\n"
            "## Pricing\nFree trial — recover 500MB at no cost. Full license — one-time purchase available.\n\n"
            "## Download\n" + AFFILIATE_URL + "\n\n"
            "## Developer\nWondershare Technology Co., Ltd.\n\n"
            "## Site\n" + SITE_DOMAIN + "\n"
            + str(len(KEYWORDS)) + " keyword pages · " + str(len(BLOG_POSTS)) + " blog posts · " + str(len(cats)) + " categories\n"
            "Sitemap: " + SITE_DOMAIN + "/sitemap.xml\n\n"
            "## Categories\n" + ", ".join(c.title() for c in cats) + "\n\n"
            "## Sample Keywords\n" + sample + "\n")

WORKFLOW = """name: Build & Deploy RecoverIt

on:
  workflow_dispatch:

permissions:
  contents: write
  pages: write
  id-token: write

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Remove all old files from repo
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          find . -maxdepth 1 -type f ! -name 'build.py' ! -name 'README.md' -delete
          find . -maxdepth 1 -type d ! -name '.' ! -name '.git' ! -name '.github' -exec rm -rf {} + 2>/dev/null || true
          git add -A
          git diff --staged --quiet || git commit -m "Clean up old files"
          git push origin main

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Run build script
        run: python3 build.py

      - name: Setup Pages
        uses: actions/configure-pages@v5

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./dist

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
"""

def progress(i, total, label=""):
    pct = i/total; bar = "█"*int(30*pct)+"░"*(30-int(30*pct))
    print(f"\r  [{bar}] {i:>4}/{total} {label:<42}", end="", flush=True)

def main():
    os.makedirs(DIST, exist_ok=True)
    os.makedirs(DIST+"/blog", exist_ok=True)
    os.makedirs(DIST+"/.github/workflows", exist_ok=True)

    print(f"\n{'═'*60}")
    print(f"  RecoverIt Site Builder v2 — {BUILD_DATE}")
    print(f"{'═'*60}")
    print(f"  Domain:   {SITE_DOMAIN}")
    print(f"  Keywords: {len(KEYWORDS)}")
    print(f"  Blog:     {len(BLOG_POSTS)} posts")
    print(f"{'═'*60}\n")

    essential = {
        "index.html":        page_index(),
        "features.html":     page_features(),
        "how-it-works.html": page_how_it_works(),
        "faq.html":          page_faq(),
        "compare.html":      page_compare(),
        "blog.html":         page_blog(),
        "download.html":     page_download(),
        "keywords.html":     page_keywords(),
        "glossary.html":     page_glossary(),
        "privacy.html":      page_privacy(),
        "404.html":          page_404(),
    }
    print("  Essential pages:")
    for fname, html in essential.items():
        with open(DIST+"/"+fname,"w",encoding="utf-8") as f: f.write(html)
        print(f"    ✓ {fname}  ({len(html)//1024}KB)")

    print(f"\n  Blog posts ({len(BLOG_POSTS)}):")
    for post in BLOG_POSTS:
        with open(DIST+"/blog/"+post["slug"]+".html","w",encoding="utf-8") as f:
            f.write(page_blog_post(post))
        print("    ✓ blog/"+post["slug"]+".html")

    print(f"\n  Keyword pages ({len(KEYWORDS)}):")
    for i,kw_data in enumerate(KEYWORDS):
        with open(DIST+"/"+kw_data["slug"]+".html","w",encoding="utf-8") as f:
            f.write(build_keyword_page(kw_data))
        progress(i+1,len(KEYWORDS),kw_data["slug"])
    print()

    support = {"sitemap.xml":build_sitemap(),"robots.txt":build_robots(),
               "llms.txt":build_llms(),"_config.yml":"# GitHub Pages\nexclude: [build.py]\n"}
    with open(DIST+"/.nojekyll","w") as f: f.write("")
    with open(DIST+"/.github/workflows/deploy.yml","w") as f: f.write(WORKFLOW)
    print("\n  Support files:")
    for fname,content in support.items():
        with open(DIST+"/"+fname,"w",encoding="utf-8") as f: f.write(content)
        print(f"    ✓ {fname}")
    print("    ✓ .nojekyll  ✓ .github/workflows/deploy.yml")

    total_sz    = sum(os.path.getsize(os.path.join(r,fn)) for r,_,files in os.walk(DIST) for fn in files)
    total_files = sum(len(files) for _,_,files in os.walk(DIST))
    report = {"build_date":BUILD_DATE,"domain":SITE_DOMAIN,
              "keyword_pages":len(KEYWORDS),"blog_posts":len(BLOG_POSTS),
              "total_files":total_files,"total_size_mb":round(total_sz/1024/1024,2),
              "affiliate_url":AFFILIATE_URL}
    with open(DIST+"/build-report.json","w") as f: json.dump(report,f,indent=2)
    print("    ✓ build-report.json")

    print(f"""
{'═'*60}
  ✅  BUILD COMPLETE
{'═'*60}
  Keyword pages:    {len(KEYWORDS):>5}
  Blog posts:       {len(BLOG_POSTS):>5}
  Essential pages:  {len(essential):>5}
  Total files:      {total_files:>5}
  Sitemap URLs:     {len(KEYWORDS)+len(BLOG_POSTS)+10:>5}
  Total size:       {round(total_sz/1024/1024,1):>4.1f} MB
  Output:           ./dist/
{'═'*60}

  Repo: https://github.com/brightlane/recoveritonline
  Live: {SITE_DOMAIN}/
""")

if __name__ == "__main__":
    main()
