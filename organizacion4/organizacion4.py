# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
# Generated by the OpenERP plugin for Dia !
from osv import fields,osv

class organizacion(osv.osv):
    """Gestión de la Organizaciones"""
    _name = 'organizacion'
    _rec_name = 'nombre'
    def _superf_fundo_org(self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        arr = []
        for o in self.browse(cr, uid, ids, context=context):
            for w in o.supeficie_ids:
                arr.append(w.tipo_id.nombre)
                for i in arr:
                    if arr.count(w.tipo_id.nombre)!=1:
                        raise osv.except_osv(('Error !'), ('haz seleccionado dos veces %s' % (w.tipo_id.nombre)))
        return  res
    _columns = {
        'control_superficie': fields.function(_superf_fundo_org, string='Personas Atendidas', type="char",size=100,  store=True),
        'nombre': fields.char('Nombre de la Organización', size=50, required=True, help='Se coloca el Nombre completo de la Organización entre ellos Comunas, Concejos Comunales, Cooperativas y Asociaciones Civiles. Ejem: Cooperativa Mixta Aracal .R.L'),
        'rif': fields.char('R.I.F.', size=15, required=True, help=' Numero de RIF de la organización. Ejem; G-20005393-3'),
        'fecha_exp': fields.datetime('Fecha de Expedición', required=True, help='Fecha de expedición o otorgamiento del R.I.F. Ejem: 15/12/2010'),
        'observacion': fields.text('Observaciones', help='Observaciones que puede tener la Organización'),
        'fundo_id': fields.many2one('fundo', 'Fundo Zamorano', required=True, help=' Colocar el Nombre del Fundo Zamorano al que Pertenece esa Organización.'),
        'supeficie_ids': fields.one2many('superficie_organizacion', 'superficie_id', 'Superficie Adjudicada de la Organización', required=True, help='Relación de la Organizacion y la Superficie'),
        'objet_id': fields.many2one('objeto', 'Objeto de la Organización', help='Objeto de la Organización'),
        'objeto': fields.text('Nombre de la Organización', size=500, required=True, help='colocar el objeto que tiene establecido esa organización en el acta constitutiva o documento de creación.'),
        'productiva_id': fields.many2one('productiva', 'Productiva', required=False, help='Relacion de la Organización con la Productividad'),
        'a_n_id': fields.many2one('estatus', 'Estatus', required=False, help='Relación de la Organización y el Estatus'),
        'org_sup_id': fields.many2one('organizacion_superior', 'Organización Superior', help='Mencionar si la organización pertenece a otra de nivel superior (Cooperativas de 2°grado, Consejo Comunal y Comuna) '),
        'documento_ids': fields.one2many('documentos', 'documento_id', 'Documentos de la Organización', help='Relación de los Documentos de la Organización'),
        'estatus_nombre': fields.selection([('activo', 'Activo'), ('no_activo', 'No Activo')], 'Estatus', help="Se refleja el estatus actual de la organización (Activa o Inactiva)", required=True, states={'activo': [('readonly', False)]}),
        'productiva_nombre': fields.selection([('productiva', 'Productiva'), ('no_productiva', 'No Productiva')], 'Productividad', help="Reflejar si la Organización se encuentra Productiva (SI o NO)", required=True, states={'productiva': [('readonly', False)]}),
    }
    _defaults = {
        'estatus_nombre': 'activo',
        'productiva_nombre': 'productiva',
        
    }
    
organizacion()

class superficie_organizacion(osv.osv):
    """Gestion de la Superficie de la Organización"""
    _name = 'superficie_organizacion'
    #_rec_name = 'superficie_id'
    _rec_name = 'espacio'
    #_rec_name = 'observacion'
    #_rec_name = 'tipo_id'
    
    _columns = {
        'superficie_id': fields.many2one('organizacion', 'Superficie', required=True, help='Superficie Adjudicada de la Organizacion'),
        'espacio': fields.integer('Hectareas de la Organización', required=True, help='Hectareas que posee la Organización'),
        'observacion': fields.text('Observaciones', help='Observaciones que puedan tener la superficie'),
        'tipo_id': fields.many2one('tipo_superficie', 'Tipo de Superficie', required=True, help='Tipo de la superficie que tienen las Hectareas'),
    }
    
superficie_organizacion()

class objeto(osv.osv):
    """Objeto de la Organización"""
    _name = 'objeto'
    _rec_name = 'nombre'
    
    _columns = {
        'nombre': fields.char('Objeto de la Organización', size=300, required=True, help='Objeto que posee la Organización'),
    }
    
objeto()

class productiva(osv.osv):
    """Gestion de Productividad"""
    _name = 'productiva'
    _rec_name = 'nombre'
    
    _columns = {
        'nombre': fields.char('Productiva', size=25, required=True, help='Si esta Productivo(a) o No Productivo(a)'),
    }
    
productiva()

class estatus(osv.osv):
    """Gestion del Estatus"""
    _name = 'estatus'
    _rec_name = 'a_n'
    
    _columns = {
        'a_n': fields.char('Estatus', size=25, required=True, help='Para saber si es Estatus, Activo(a) o No Activo(a)'),
    }
    
estatus()

class organizacion_superior(osv.osv):
    """Gestion de la Organización Superior"""
    _name = 'organizacion_superior'
    _rec_name = 'nombre'
    #_rec_name = 'rif'
    #_rec_name = 'direccion'
    
    _columns = {
        'nombre': fields.char('Nombre de la Organización Superior', size=100, required=True, help='Nombre de la Organización Superior '),
        'rif': fields.char('R.I.F.', size=20, required=True, help='RIF de la Organización Superior'),
        'direccion': fields.char('Dirección', size=200, required=True, help='Dirección a la que pertenece esta Organizacion'),
        'persona_contacto': fields.char('Persona Contacto', size=200, required=True, help='Persona de contacto que posee la Organizacion Superior'),
        'telefono': fields.char('Numero de Telefono', size=50, required=True, help='Telefono de contacto de la Persona'),
        'correo': fields.char('Correo Electronico', size=50, required=False, help='Correo de contacto de la Persona'),
    }
    
organizacion_superior()

class persona(osv.osv):
    """Tabla de Prueba Persona"""
    _name = 'persona'
    _rec_name = 'cedula'
    #_rec_name = 'nombres'
    
    _columns = {
        'cedula': fields.integer('Cedula', required=True, help='Cedula de Persona'),
        'nombres': fields.char('Nombres', size=50, required=True, help='Nombre de la Persona'),
        'telefono': fields.char('Telefono', size=50, required=True, help='Telefono de la Persona'),
        'correo': fields.char('Correo', size=50, required=False, help='Correo de la Persona'),
        
    }
    
    
    
persona()

class documentos(osv.osv):
    """Gestion de Documentos"""
    _name = 'documentos'
    #_rec_name = 'documento_id'
    _rec_name = 'codigo'
    #_rec_name = 'fecha_exp'
    #_rec_name = 'fecha_ven'
    #_rec_name = 'persona_id'
    #_rec_name = 'tipo_id'
    #_rec_name = 'legal_id'
    
    _columns = {
        'documento_id': fields.many2one('organizacion', 'Documentos de la Organización', help='Documentos que posee la Organización'),
        'codigo': fields.char('Codigo del Documento', size=50, required=True, help='se refleja el código de los documentos mas relevantes de la organización (N° registro ante Sunacoop o N° registro ante el ministerio de las Comunas)'),
        'fecha_exp': fields.datetime('Fecha de Expedición', required=True, help='Se debe reflejar la fecha de expedición o otorgamiento  del documento. Ejem: 15/12/2010'),
        'fecha_ven': fields.datetime('Fecha de Vencimiento',  required=False, help='Se debe colocar la fecha de vencimiento del documento Ejem: 15/12/2016 (Si el documento posee dicha fecha)'),
        'persona_id': fields.many2one('persona', 'Persona Encargada del Documento', required=True, help=' Se reflejara el representante legal que sale en el documento'),
        'tipo_id': fields.many2one('tipo_documento', 'Tipo de Documento', help='Seleccionar el Tipo de Documento el cual es el documento (Libro, Acta, ect.)'),
        'legal_id': fields.many2one('documentos_legales', 'Nombre de los Documentos Legales', help='Se reflejara el tipo de documento registrado (Acta constitutiva, acta de fiel cumplimiento, etc) '),
    }
    
documentos()

class tipo_documento(osv.osv):
    """Gestión de los Tipos de Documentos"""
    _name = 'tipo_documento'
    _rec_name = 'nombre'
    
    _columns = {
        'nombre': fields.char('Tipo del Documento', size=100, required=True, help='Nombre que poseé el tipo de documento'),
    }
    
tipo_documento()

class documentos_legales(osv.osv):
    """Gestión de Documentos Legales"""
    _name = 'documentos_legales'
    _rec_name = 'nombre'
    #_rec_name = 'tipo_id'
    
    _columns = {
        'nombre': fields.char('Documentos Legales', size=50, required=True, help='Documentos legales'),
        'tipo_id': fields.many2one('tipo_documento', 'Tipo de Documento', help='Relación de los Documentos Legales con los Tipos de Documentos'),
    }
    
documentos_legales()

