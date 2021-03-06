# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/common/segments.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v0.proto.enums import ad_network_type_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_ad__network__type__pb2
from google.ads.google_ads.v0.proto.enums import conversion_attribution_event_type_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_conversion__attribution__event__type__pb2
from google.ads.google_ads.v0.proto.enums import day_of_week_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_day__of__week__pb2
from google.ads.google_ads.v0.proto.enums import device_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_device__pb2
from google.ads.google_ads.v0.proto.enums import hotel_date_selection_type_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_hotel__date__selection__type__pb2
from google.ads.google_ads.v0.proto.enums import month_of_year_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_month__of__year__pb2
from google.ads.google_ads.v0.proto.enums import placeholder_type_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_placeholder__type__pb2
from google.ads.google_ads.v0.proto.enums import search_term_match_type_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_search__term__match__type__pb2
from google.ads.google_ads.v0.proto.enums import slot_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_slot__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/common/segments.proto',
  package='google.ads.googleads.v0.common',
  syntax='proto3',
  serialized_options=_b('\n\"com.google.ads.googleads.v0.commonB\rSegmentsProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/common;common\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V0.Common\312\002\036Google\\Ads\\GoogleAds\\V0\\Common\352\002\"Google::Ads::GoogleAds::V0::Common'),
  serialized_pb=_b('\n3google/ads/googleads_v0/proto/common/segments.proto\x12\x1egoogle.ads.googleads.v0.common\x1a\x39google/ads/googleads_v0/proto/enums/ad_network_type.proto\x1aKgoogle/ads/googleads_v0/proto/enums/conversion_attribution_event_type.proto\x1a\x35google/ads/googleads_v0/proto/enums/day_of_week.proto\x1a\x30google/ads/googleads_v0/proto/enums/device.proto\x1a\x43google/ads/googleads_v0/proto/enums/hotel_date_selection_type.proto\x1a\x37google/ads/googleads_v0/proto/enums/month_of_year.proto\x1a:google/ads/googleads_v0/proto/enums/placeholder_type.proto\x1a@google/ads/googleads_v0/proto/enums/search_term_match_type.proto\x1a.google/ads/googleads_v0/proto/enums/slot.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xa4\r\n\x08Segments\x12W\n\x0f\x61\x64_network_type\x18\x03 \x01(\x0e\x32>.google.ads.googleads.v0.enums.AdNetworkTypeEnum.AdNetworkType\x12\x8b\x01\n!conversion_attribution_event_type\x18\x02 \x01(\x0e\x32`.google.ads.googleads.v0.enums.ConversionAttributionEventTypeEnum.ConversionAttributionEventType\x12*\n\x04\x64\x61te\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12K\n\x0b\x64\x61y_of_week\x18\x05 \x01(\x0e\x32\x36.google.ads.googleads.v0.enums.DayOfWeekEnum.DayOfWeek\x12@\n\x06\x64\x65vice\x18\x01 \x01(\x0e\x32\x30.google.ads.googleads.v0.enums.DeviceEnum.Device\x12>\n\x19hotel_booking_window_days\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x34\n\x0fhotel_center_id\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x39\n\x13hotel_check_in_date\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12Z\n\x1ahotel_check_in_day_of_week\x18\t \x01(\x0e\x32\x36.google.ads.googleads.v0.enums.DayOfWeekEnum.DayOfWeek\x12\x30\n\nhotel_city\x18\n \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\x0bhotel_class\x18\x0b \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x33\n\rhotel_country\x18\x0c \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12s\n\x19hotel_date_selection_type\x18\r \x01(\x0e\x32P.google.ads.googleads.v0.enums.HotelDateSelectionTypeEnum.HotelDateSelectionType\x12\x39\n\x14hotel_length_of_stay\x18\x0e \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x31\n\x0bhotel_state\x18\x0f \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12)\n\x04hour\x18\x10 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12+\n\x05month\x18\x11 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12Q\n\rmonth_of_year\x18\x12 \x01(\x0e\x32:.google.ads.googleads.v0.enums.MonthOfYearEnum.MonthOfYear\x12\x36\n\x10partner_hotel_id\x18\x13 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\\\n\x10placeholder_type\x18\x14 \x01(\x0e\x32\x42.google.ads.googleads.v0.enums.PlaceholderTypeEnum.PlaceholderType\x12-\n\x07quarter\x18\x15 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12j\n\x16search_term_match_type\x18\x16 \x01(\x0e\x32J.google.ads.googleads.v0.enums.SearchTermMatchTypeEnum.SearchTermMatchType\x12:\n\x04slot\x18\x17 \x01(\x0e\x32,.google.ads.googleads.v0.enums.SlotEnum.Slot\x12*\n\x04week\x18\x18 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12)\n\x04year\x18\x19 \x01(\x0b\x32\x1b.google.protobuf.Int32ValueB\xe8\x01\n\"com.google.ads.googleads.v0.commonB\rSegmentsProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/common;common\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V0.Common\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V0\\Common\xea\x02\"Google::Ads::GoogleAds::V0::Commonb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_ad__network__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_conversion__attribution__event__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_day__of__week__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_device__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_hotel__date__selection__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_month__of__year__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_placeholder__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_search__term__match__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_slot__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_SEGMENTS = _descriptor.Descriptor(
  name='Segments',
  full_name='google.ads.googleads.v0.common.Segments',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ad_network_type', full_name='google.ads.googleads.v0.common.Segments.ad_network_type', index=0,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conversion_attribution_event_type', full_name='google.ads.googleads.v0.common.Segments.conversion_attribution_event_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date', full_name='google.ads.googleads.v0.common.Segments.date', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='day_of_week', full_name='google.ads.googleads.v0.common.Segments.day_of_week', index=3,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device', full_name='google.ads.googleads.v0.common.Segments.device', index=4,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hotel_booking_window_days', full_name='google.ads.googleads.v0.common.Segments.hotel_booking_window_days', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hotel_center_id', full_name='google.ads.googleads.v0.common.Segments.hotel_center_id', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hotel_check_in_date', full_name='google.ads.googleads.v0.common.Segments.hotel_check_in_date', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hotel_check_in_day_of_week', full_name='google.ads.googleads.v0.common.Segments.hotel_check_in_day_of_week', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hotel_city', full_name='google.ads.googleads.v0.common.Segments.hotel_city', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hotel_class', full_name='google.ads.googleads.v0.common.Segments.hotel_class', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hotel_country', full_name='google.ads.googleads.v0.common.Segments.hotel_country', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hotel_date_selection_type', full_name='google.ads.googleads.v0.common.Segments.hotel_date_selection_type', index=12,
      number=13, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hotel_length_of_stay', full_name='google.ads.googleads.v0.common.Segments.hotel_length_of_stay', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hotel_state', full_name='google.ads.googleads.v0.common.Segments.hotel_state', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hour', full_name='google.ads.googleads.v0.common.Segments.hour', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='month', full_name='google.ads.googleads.v0.common.Segments.month', index=16,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='month_of_year', full_name='google.ads.googleads.v0.common.Segments.month_of_year', index=17,
      number=18, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partner_hotel_id', full_name='google.ads.googleads.v0.common.Segments.partner_hotel_id', index=18,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='placeholder_type', full_name='google.ads.googleads.v0.common.Segments.placeholder_type', index=19,
      number=20, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quarter', full_name='google.ads.googleads.v0.common.Segments.quarter', index=20,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='search_term_match_type', full_name='google.ads.googleads.v0.common.Segments.search_term_match_type', index=21,
      number=22, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slot', full_name='google.ads.googleads.v0.common.Segments.slot', index=22,
      number=23, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='week', full_name='google.ads.googleads.v0.common.Segments.week', index=23,
      number=24, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='year', full_name='google.ads.googleads.v0.common.Segments.year', index=24,
      number=25, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=661,
  serialized_end=2361,
)

_SEGMENTS.fields_by_name['ad_network_type'].enum_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_ad__network__type__pb2._ADNETWORKTYPEENUM_ADNETWORKTYPE
_SEGMENTS.fields_by_name['conversion_attribution_event_type'].enum_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_conversion__attribution__event__type__pb2._CONVERSIONATTRIBUTIONEVENTTYPEENUM_CONVERSIONATTRIBUTIONEVENTTYPE
_SEGMENTS.fields_by_name['date'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_SEGMENTS.fields_by_name['day_of_week'].enum_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_day__of__week__pb2._DAYOFWEEKENUM_DAYOFWEEK
_SEGMENTS.fields_by_name['device'].enum_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_device__pb2._DEVICEENUM_DEVICE
_SEGMENTS.fields_by_name['hotel_booking_window_days'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_SEGMENTS.fields_by_name['hotel_center_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_SEGMENTS.fields_by_name['hotel_check_in_date'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_SEGMENTS.fields_by_name['hotel_check_in_day_of_week'].enum_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_day__of__week__pb2._DAYOFWEEKENUM_DAYOFWEEK
_SEGMENTS.fields_by_name['hotel_city'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_SEGMENTS.fields_by_name['hotel_class'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_SEGMENTS.fields_by_name['hotel_country'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_SEGMENTS.fields_by_name['hotel_date_selection_type'].enum_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_hotel__date__selection__type__pb2._HOTELDATESELECTIONTYPEENUM_HOTELDATESELECTIONTYPE
_SEGMENTS.fields_by_name['hotel_length_of_stay'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_SEGMENTS.fields_by_name['hotel_state'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_SEGMENTS.fields_by_name['hour'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_SEGMENTS.fields_by_name['month'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_SEGMENTS.fields_by_name['month_of_year'].enum_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_month__of__year__pb2._MONTHOFYEARENUM_MONTHOFYEAR
_SEGMENTS.fields_by_name['partner_hotel_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_SEGMENTS.fields_by_name['placeholder_type'].enum_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_placeholder__type__pb2._PLACEHOLDERTYPEENUM_PLACEHOLDERTYPE
_SEGMENTS.fields_by_name['quarter'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_SEGMENTS.fields_by_name['search_term_match_type'].enum_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_search__term__match__type__pb2._SEARCHTERMMATCHTYPEENUM_SEARCHTERMMATCHTYPE
_SEGMENTS.fields_by_name['slot'].enum_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_slot__pb2._SLOTENUM_SLOT
_SEGMENTS.fields_by_name['week'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_SEGMENTS.fields_by_name['year'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
DESCRIPTOR.message_types_by_name['Segments'] = _SEGMENTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Segments = _reflection.GeneratedProtocolMessageType('Segments', (_message.Message,), dict(
  DESCRIPTOR = _SEGMENTS,
  __module__ = 'google.ads.googleads_v0.proto.common.segments_pb2'
  ,
  __doc__ = """Segment only fields.
  
  
  Attributes:
      ad_network_type:
          Ad network type.
      conversion_attribution_event_type:
          Conversion attribution event type.
      date:
          Date to which metrics apply. yyyy-MM-dd format, e.g.,
          2018-04-17.
      day_of_week:
          Day of the week, e.g., MONDAY.
      device:
          Device to which metrics apply.
      hotel_booking_window_days:
          Hotel booking window in days.
      hotel_center_id:
          Hotel center ID.
      hotel_check_in_date:
          Hotel check-in date. Formatted as yyyy-MM-dd.
      hotel_check_in_day_of_week:
          Hotel check-in day of week.
      hotel_city:
          Hotel city.
      hotel_class:
          Hotel class.
      hotel_country:
          Hotel country.
      hotel_date_selection_type:
          Hotel date selection type.
      hotel_length_of_stay:
          Hotel length of stay.
      hotel_state:
          Hotel state.
      hour:
          Hour of day as a number between 0 and 23, inclusive.
      month:
          Month as represented by the date of the first day of a month.
          Formatted as yyyy-MM-dd.
      month_of_year:
          Month of the year, e.g., January.
      partner_hotel_id:
          Partner hotel ID.
      placeholder_type:
          Placeholder type. This is only used with feed item metrics.
      quarter:
          Quarter as represented by the date of the first day of a
          quarter. Uses the calendar year for quarters, e.g., the second
          quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd.
      search_term_match_type:
          Match type of the keyword that triggered the ad, including
          variants.
      slot:
          Position of the ad.
      week:
          Week as defined as Monday through Sunday, and represented by
          the date of Monday. Formatted as yyyy-MM-dd.
      year:
          Year, formatted as yyyy.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.common.Segments)
  ))
_sym_db.RegisterMessage(Segments)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
