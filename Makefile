VERSION = `grep plugin.video.hromadske.tv plugin.video.hromadske.tv/addon.xml | sed s/".*version=\""// | sed s/"\".*"//`


zip:
	rm -rf build/plugin.video.hromadske.tv*
	mkdir -p build/
	cp -R plugin.video.hromadske.tv build/
	cd build && find . -name "*.pyc" -delete && find . -name "*~" -delete && zip -r plugin.video.hromadske.tv-$(VERSION).zip plugin.video.hromadske.tv
