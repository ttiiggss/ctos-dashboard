import re
from pathlib import Path

def test_ctos_dashboard_structure():
    html_file = Path(__file__).parent / "index.html"
    assert html_file.exists(), "index.html missing"
    
    content = html_file.read_text(encoding="utf-8")
    
    # Check Leaflet & CSS dependencies
    assert "leaflet@1.9.4" in content, "Leaflet CDN dependency missing"
    assert "cartodb" in content.lower(), "CartoDB basemap tile URL missing"
    
    # Check HUD elements
    assert "hud-coords" in content, "HUD coordinates display element missing"
    assert "hud-target-count" in content, "HUD target counter element missing"
    
    # Check Kanban structure
    assert "kanban-board" in content, "Kanban board container missing"
    assert 'id="col-queue"' in content, "Queue column missing"
    assert 'id="col-active"' in content, "Active column missing"
    assert 'id="col-resolved"' in content, "Resolved column missing"
    
    # Check Core JS functions
    assert "function initMap()" in content, "initMap function missing"
    assert "function renderBoard()" in content, "renderBoard function missing"
    assert "function advanceStatus(" in content, "advanceStatus function missing"
    assert "function fetchUSGSFeed()" in content, "fetchUSGSFeed function missing"

if __name__ == "__main__":
    test_ctos_dashboard_structure()
    print("ctOS Dashboard structure & script check: PASS")
