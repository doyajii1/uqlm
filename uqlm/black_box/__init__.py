# Copyright 2025 CVS Health and/or one of its affiliates
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from uqlm.black_box.bert import BertScorer

from uqlm.black_box.bleurt import BLEURTScorer  # deprecated in v0.2.0
from uqlm.black_box.cosine import CosineScorer
from uqlm.black_box.match import MatchScorer
from uqlm.black_box.nli import NLIScorer

__all__ = ["BertScorer", "CosineScorer", "BLEURTScorer", "MatchScorer", "NLIScorer"]
