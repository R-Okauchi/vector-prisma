from builtins import str as _str

from prisma import types
from typing_extensions import TypedDict

from .vector_type import Vector


class NetisEmbeddingOptionalCreateInput(TypedDict, total=False):
    """Optional arguments to the NetisEmbedding create method"""

    id: _str
    netis_id: _str
    netis: "types.NetisCreateNestedWithoutRelationsInput"


class NetisEmbeddingCreateInput(NetisEmbeddingOptionalCreateInput):
    """Required arguments to the NetisEmbedding create method"""

    vec: Vector


class NetisEmbeddingUpdateInput(TypedDict, total=False):
    """Optional arguments for updating a record"""

    id: _str
    vec: Vector
    netis: "types.NetisUpdateOneWithoutRelationsInput"


class NetisEmbeddingUpsertInput(TypedDict):
    create: "NetisEmbeddingCreateInput"
    update: "NetisEmbeddingUpdateInput"


class OutlineEmbeddingOptionalCreateInput(TypedDict, total=False):
    """Optional arguments to the OutlineEmbedding create method"""

    id: _str
    theme_id: _str
    theme: "types.ThemeCreateNestedWithoutRelationsInput"
    outline_id: _str
    outline: "types.OutlineCreateNestedWithoutRelationsInput"


class OutlineEmbeddingCreateInput(OutlineEmbeddingOptionalCreateInput):
    """Required arguments to the OutlineEmbedding create method"""

    vec: Vector


class OutlineEmbeddingUpdateInput(TypedDict, total=False):
    """Optional arguments for updating a record"""

    id: _str
    vec: Vector
    theme: "types.ThemeUpdateOneWithoutRelationsInput"
    outline: "types.OutlineUpdateOneWithoutRelationsInput"


class OutlineEmbeddingUpsertInput(TypedDict):
    create: "OutlineEmbeddingCreateInput"
    update: "OutlineEmbeddingUpdateInput"
