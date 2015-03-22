import sys
sys.path.append('.')
import neurio

from distutils.core import setup
setup(
  name = 'neurio',
  packages = ['neurio'],
  version = str(neurio.__version__),
  description = 'Neurio energy sensor and appliance detection platform API',
  author = 'Jordan Husney',
  author_email = 'jordan.husney@gmail.com',
  url = 'https://github.com/jordanh/neurio-python',
  download_url = 'https://github.com/peterldowns/mypackage/tarball/0.1',
  keywords = ['neurio', 'iot', 'energy', 'sensor', 'smarthome'],
  classifiers = [],
)