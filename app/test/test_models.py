import pytest

from app.models import Producto, Categoria


@pytest.mark.django_db
def test_producto_str_and_relation():
    categoria = Categoria.objects.create(nombre="coches")
    producto = Producto.objects.create(nombre="bugatti",unidades=15,precio=1500, categoria=categoria)
    assert str(producto) == "bugatti"
    assert producto.categoria is categoria


# import pytest
# from empleados.models import Departamento, Empleado
# @pytest.mark.django_db
# def test_empleado_str_and_relation():
# dep = Departamento.objects.create(nombre="IT")
# emp = Empleado.objects.create(nombre="Ana", departamento=dep)
# assert str(emp) == "Ana"
# assert emp.departamento is dep